import random
import librosa
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import librosa.display

def visualizer(file):
    #Select audio files at random to compare and display
    #file_list = [f for f in listdir(".") if isfile(join(".", f))]
    #audio_data = random.sample(file_lis, 2)
    #print("Audio files chosen: " + ", ".join(audio_data))

    #This returns an audio time series as a numpy array with a default sampling rate(sr) of 22KHZ
    x,sr0 = librosa.load(file, sr=None)
    #y,sr1 = librosa.load(audio_data[1], sr=None)

    #We can change this behavior by resampling at sr=44.1KHz.
    x,sr0 = librosa.load(file, sr=44000)
    print(x)
    #return x
    #y,sr1 = librosa.load(audio_data[1], sr=44000)

    #Plot the sampled signals against each other
    #plt.figure(figsize=(14, 5))
    #return librosa.display.waveplot(x, sr=44000)
    return x