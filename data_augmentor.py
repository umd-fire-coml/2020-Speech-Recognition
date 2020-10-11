import numpy as np
import librosa


class DataAugmentation:

    def __init__(self, noise_factor=2, sampling_rate=8000,
                 shift_max=1, shift_direction='both',
                 pitch_factor=2, speed_factor=1.5, file_path="", data=0):
        """ Initialization

        :param noise_factor: amount of noise to be injected (0-5).
        :param sampling_rate: frequency of the sample in Hz (Generally 8000Hz).
        :param shift_max: how much to shift the audio sample by (number of seconds).
        :param shift_direction: In which direction to shift audio (left, right, both).
        :param pitch_factor: How much to change the pitch of audio (-8 to 8).
        :param speed_factor: Changes speed of the audio (0 to 2)
        :param file_path: path of audio_file
        :param data: Audio file as Numpy array
        """

        self.noise_factor = noise_factor
        self.sampling_rate = sampling_rate
        self.shift_max = shift_max
        self.shift_direction = shift_direction
        self.pitch_factor = pitch_factor
        self.speed_factor = speed_factor
        self.file_path = file_path
        self.data = load_data()

    def noise_injection(self):
        """
        Injects random values into the audio array which counts as background
        :return: Augmented data
        """

        noise = np.random.randn(len(self.data))
        augmented_data = data + self.noise_factor * noise

        # Cast back to same data type

        augmented_data = augmented_data.astype(type(data[0]))
        return augmented_data

    def shifting_time(self):

        """
        Shifting Right is shifting backwards and shifting left is
        shifting forward. Here shift_max is in seconds.

        :return: augmented_data
        """

        shift = np.random.randint(self.sampling_rate * self.shift_max)

        if self.shift_direction == 'right':
            shift = -shift

        elif self.shift_direction == 'both':  # If want to do random shifting.
            direction = np.random.randint(0, 2)
            if direction == 1:
                shift = -shift

        augmented_data = np.roll(self.data, shift)

        # Silence heading/ tailing
        if shift > 0:
            augmented_data[:shift] = 0
        else:
            augmented_data[shift:] = 0

        return augmented_data

    def change_pitch(self):

        """
        pitch_factor will change the pitch up if positive and down if negative.
        :return augmented_data: returns an ndArray.
        """
        augmented_data = librosa.effects.pitch_shift(data, self.sampling_rate, self.pitch_factor)
        return augmented_data

    def change_speed(self):
        """
        Speed_factor should be a float from 0 to 2
        :return: Augmented data
        """
        return librosa.effects.time_stretch(self.data, self.speed_factor)

    def load_data(self):
        """
        Loads the data into file
        :return: Augmented data
        """
        data = librosa.load(self.file_path, sr=None)

        return data
