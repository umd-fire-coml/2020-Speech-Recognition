import numpy as np
import tensorflow as tf
from tensorflow import keras

import re
import string
import random
import librosa
import python_speech_features
from os import listdir
from alphabet import Alphabet
from os.path import isfile, join
from lyrics_extractor import SongLyrics

class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'

    def __init__(self, path_prefix, list_IDs, labels, batch_size, dim, n_channels,
                 n_classes, shuffle):
        'Initialization'
        self.path_prefix = path_prefix
        self.dim = dim
        self.batch_size = batch_size
        self.labels = np.array(labels)
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
        X = self.__data_generation(list_IDs_temp, indexes) #,y when other stuff is uncommented
        
        return X

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, list_IDs_temp, indexes):
        'Generates data containing batch_size samples' 
        # X : (n_samples, *dim, n_channels)
        # Initialization
        X = []

        # Generate data
        for i, ID in enumerate(list_IDs_temp):
            X.append(self.load_audio(join(self.path_prefix,ID)))

        X = self.pad_and_transpose(X)
        X = self.align(X)

        alphabet = Alphabet("alphabet.txt")
        #lyrics = alphabet.get_batch_labels(self.fetch_lyrics(self.labels))
        lyrics = alphabet.get_batch_labels(self.labels[indexes])
        #lyrics = self.align(lyrics)

        return (X, lyrics)

    def load_audio(self, audio_file_path):
        """Load audio to numpy array and return it"""
        """ Use `python_speech_"features` lib to extract MFCC features from the audio file. """
        audio, fs = librosa.load(audio_file_path, sr=16000)
        audio = (audio * 32768).astype("int16")
        return audio

    def align(self, arrays, default=0):
        """ Pad arrays along time dimensions. Return the single array (batch_size, time, features). """
        max_array = max(arrays, key=len)
        X = np.full(shape=[len(arrays), *max_array.shape], fill_value=default, dtype=np.float64)
        for index, array in enumerate(arrays):
            time_dim, features_dim = array.shape
            X[index, :time_dim] = array
        return X

    def pad_and_transpose(self, audio_list):
        """Pad audio files with zeroes to ensure even length"""
        """Use `python_speech_"features` lib to extract MFCC features from the audio file."""
        max_array = max(audio_list, key=len)
        max_len = len(max_array)
        aug_list = []
        conf = {"winfunc": np.hamming, "winlen": 0.025, "winstep": .01, "nfilt": 80}
        for audio in audio_list:
            audio = np.concatenate((audio, np.zeros((max_len - len(audio),), dtype=int)))
            feat, energy = python_speech_features.fbank(audio, samplerate=16000, **conf)
            features = np.log(feat)
            aug_list.append(features)
        return aug_list

    def fetch_lyrics(self, labels):
        keys = open("keys.txt").readlines()
        api_key = keys[0]
        engine_id = keys[1]
        extract_lyrics = SongLyrics(api_key, engine_id)
        lyrics = []
        for song in labels:
            lyric = extract_lyrics.get_lyrics(song)['lyrics']
            lyric = re.sub("[\(\[].*?[\)\]]", "", lyrics)
            lyric = lyric.replace('\n', ' ').lower()
            lyric = lyric.translate(str.maketrans('', '', string.punctuation))
            lyrics.append(lyric)
        lyrics.append(lyric)
        return lyrics






