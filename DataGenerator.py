import numpy as np
import keras

import random
import librosa
from os import listdir
from os.path import isfile, join

class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self, list_IDs, labels, batch_size, dim, n_channels,
                 n_classes, shuffle):
        'Initialization'
        self.dim = dim
        self.batch_size = batch_size
        self.labels = labels
        self.list_IDs = list_IDs
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.shuffle = shuffle
        self.on_epoch_end()

    def __len__(self):
        'Denotes the number of batches per epoch'
        return int(np.floor(len(self.list_IDs) / self.batch_size))

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]

        # Find list of IDs
        list_IDs_temp = [self.list_IDs[k] for k in indexes]

        # Generate data
        X = self.__data_generation(list_IDs_temp) #,y when other stuff is uncommented

        return X#, y

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, list_IDs_temp):
        'Generates data containing batch_size samples' # X : (n_samples, *dim, n_channels)
        # Initialization
        
        curr_len = 0
        for i,ID in enumerate(list_IDs_temp):
          print(ID)
          curr_len = len(self.load_audio('grace_data/amazing_grace/'+ID))
        print(curr_len)
        X = np.empty((self.batch_size, curr_len))
        #y = np.empty((self.batch_size), dtype=int)

        # Generate data
        for i, ID in enumerate(list_IDs_temp):
            # Store sample
            #self.load_audio('grace_data/amazing_grace/312087870_108215812.m4a')
            X[i,] = self.load_audio('grace_data/amazing_grace/'+ID)

            # Store class
            #y[i] = self.labels[ID]

        return X#, keras.utils.to_categorical(y, num_classes=self.n_classes)

    def load_audio(self,audio_file_path):
        """Load audio to numpy array and return it
        """
        x,sr = librosa.load(audio_file_path, sr = None)
        return x