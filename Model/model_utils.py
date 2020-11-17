from tensorflow import config

from typing import List
from tensorflow.keras import Model
import tensorflow
from tensorflow import expand_dims, squeeze
from tensorflow.compat.v1.keras.layers import CuDNNLSTM
from tensorflow.keras.layers import Input, Lambda, LSTM, Bidirectional, Dense, ReLU, \
    TimeDistributed, BatchNormalization, Dropout, ZeroPadding2D, Conv2D, Reshape

import tensorflow as tf
from tensorflow.keras.optimizers import Optimizer, SGD, Adam

from functools import partial
from tensorflow.keras import backend as K

from tensorflow.keras.callbacks import Callback, TerminateOnNaN, LearningRateScheduler, ReduceLROnPlateau, History
import importlib
import callbacks
importlib.reload(callbacks)
from callbacks import ResultKeeper, CustomModelCheckpoint, CustomTensorBoard, CustomEarlyStopping
import numpy as np

def get_model(gpus):
    input_dim = 80
    is_gpu = len(gpus) > 0
    output_dim = 28
    context = 7
    units = 1024
    dropouts = [0.1, .1, 0]
    #random_state = 1

    #np.random.seed(1)
    #tensorflow.random.set_seed(random_state)
    input_tensor = Input([None, input_dim], name='X')                           # Define input tensor [time, features]
    x = Lambda(expand_dims, arguments=dict(axis=-1))(input_tensor)              # Add 4th dim (channel)
    x = ZeroPadding2D(padding=(context, 0))(x)                                  # Fill zeros around time dimension
    receptive_field = (2*context + 1, input_dim)                                # Take into account fore/back-ward context
    x = Conv2D(filters=units, kernel_size=receptive_field)(x)                   # Convolve signal in time dim
    x = Lambda(squeeze, arguments=dict(axis=2))(x)                              # Squeeze into 3rd dim array
    x = ReLU(max_value=20)(x)                                                   # Add non-linearity
    x = Dropout(rate=dropouts[0])(x)                                            # Use dropout as regularization

    x = TimeDistributed(Dense(units))(x)                                        # 2nd and 3rd FC layers do a feature
    x = ReLU(max_value=20)(x)                                                   # extraction base on the context
    x = Dropout(rate=dropouts[1])(x)

    x = TimeDistributed(Dense(units))(x)
    x = ReLU(max_value=20)(x)
    x = Dropout(rate=dropouts[2])(x)

    x = Bidirectional(CuDNNLSTM(units, return_sequences=True) if is_gpu else     # LSTM handle long dependencies
                        LSTM(units, return_sequences=True, ),
                        merge_mode='sum')(x)

    output_tensor = TimeDistributed(Dense(output_dim, activation='softmax'))(x)  # Return at each time step prob along characters

    model = Model(inputs=input_tensor, outputs=output_tensor)
    return model

def ctc_loss(y, y_hat):
    print("calculating loss")
    def get_length(tensor):
        lengths = tf.reduce_sum(tf.ones_like(tensor), 1)
        return tf.reshape(tf.cast(lengths, tf.int32), [-1, 1])


    sequence_length = get_length(tf.reduce_max(y_hat, 2))
    label_length = get_length(y)
    ret = tf.keras.backend.ctc_batch_cost(y, y_hat, sequence_length, label_length)
    print(ret)
    return ret

def get_optimizer():
    optimizer = Adam(
        learning_rate=0.001,
        beta_1=0.9,
        beta_2=0.999,
        epsilon=1e-07,
        amsgrad=False,
        name="Adam",
    )

    return optimizer

def get_compiled_model():
    list_physical_devices = config.list_physical_devices
    model_dir = "models/"
    gpus = list_physical_devices("GPU")
    model = get_model(gpus)
    loss = ctc_loss
    optimizer = get_optimizer()
    gpus_num = len(gpus)
    compiled_model = multi_gpu_model(model, gpus_num) if gpus_num > 1 else model
    y = Input(name='y', shape=[None], dtype='int32')
    compiled_model.compile(optimizer, loss, target_tensors=[y])

    return compiled_model

def batch_tensorflow_decode(y_hat, decoder, alphabet):
    """ Enable to batch decode using tensorflow decoder. """
    labels, = decoder([y_hat])
    return alphabet.get_batch_transcripts(labels)

def get_decoder(output_tensor, alphabet):
    def get_length(tensor):
        lengths = tf.reduce_sum(tf.ones_like(tensor), 1)
        return tf.cast(lengths, tf.int32)

    sequence_length = get_length(tf.reduce_max(output_tensor, 2))
    top_k_decoded, _ = K.ctc_decode(output_tensor, sequence_length, greedy=False, beam_width=64)
    print(top_k_decoded[0])
    decoder = K.function([output_tensor], [top_k_decoded[0]])
    return partial(batch_tensorflow_decode, alphabet=alphabet, decoder=decoder)


def get_callbacks():
    callbacks = []
    callbacks.append(TerminateOnNaN())
    callbacks.append(ResultKeeper("results.bin"))
    callbacks.append(CustomModelCheckpoint('checkpoints'))
    callbacks.append(CustomTensorBoard('tensorboard'))
    callbacks.append(CustomEarlyStopping(mini_targets={5: 200, 10:100}, monitor="val_loss", patience=3))
    #lr_decay = lambda epoch, lr: lr / np.power(.1, epoch)
    #callbacks.append(LearningRateScheduler(lr_decay, verbose= 1))
    return callbacks


