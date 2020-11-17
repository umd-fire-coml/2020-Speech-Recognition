import sys
sys.path.append("Model")
from Model.alphabet import Alphabet
alphabet = Alphabet("Model/alphabet.txt")

from Model.model_utils import get_compiled_model
from Model.model_utils import get_decoder
from Model.model_utils import get_callbacks

compiled_model = get_compiled_model()
callbacks = get_callbacks()
decoder = get_decoder(compiled_model.output, alphabet)

compiled_model.load_weights("Model/checkpoints/weights.05-210.04.hdf5")

import numpy as np
import python_speech_features
import librosa

conf = {"winfunc": np.hamming, "winlen": 0.025, "winstep": .01, "nfilt": 80}

def get_features(files):
    mfccs = [make_features(file) for file in files]
    X = align(mfccs)
    return X

def make_features(file_path):
    """ Use `python_speech_"features` lib to extract MFCC features from the audio file. """
    audio, fs = librosa.load(file_path, sr=16000)
    audio = (audio * 32768).astype("int16")
    feat, energy = python_speech_features.fbank(audio, samplerate=fs, **conf)
    features = np.log(feat)
    return features

def align(arrays, default=0):
    """ Pad arrays along time dimensions. Return the single array (batch_size, time, features). """
    max_array = max(arrays, key=len)
    X = np.full(shape=[len(arrays), *max_array.shape], fill_value=default, dtype=np.float64)
    for index, array in enumerate(arrays):
        time_dim, features_dim = array.shape
        X[index, :time_dim] = array
    return X


def parse_audio(file):
    files = [file]
    audio, fs = librosa.load(files[0], sr=16000)
    X = get_features(files)
    y = compiled_model.predict_on_batch(X)
    print("HERE:")
    print(type(decoder(y)))
    return decoder(y)[0]