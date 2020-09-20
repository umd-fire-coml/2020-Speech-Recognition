# Research

This folder contains research papers we have read and notes

## Papers

### [Noise Estimation and Noise Removal Techniques](Noise_Estimation_And_Noise_Removal_Techniques.pdf)

[Original Link Here](https://link.springer.com/chapter/10.1007/978-3-642-16327-2_40)
This paper focuses on voice activity detection and background noise removal techniques. Branching from the standard assumption that noise filtering requires VADs, Shrawanker and Thakare explore RLS (a recursive least squares algorithm) combined with a pairing of a Hidden Markov Model and Bayesian Network to fuse pattern recognition outputs. This method of recursively training clusters and iteratively moving between them based on a probability distribution has almost entirely eliminated background noise in dynamic settings.

### [Text-Guided Image-to-Image Translation](Text-Guded_Image-to-Image_Translation.pdf)

[Original Link Here](https://arxiv.org/pdf/2008.04200.pdf)
In this paper, Liu et al. utilize GANs to facilitate text-driven image manipulation. Aiming to eliminate the discomfort associated with image editing on portable devices for impaired users, this approach uses neural networks to identify the pixels to be edited, and processes the text that the user inputs to make changes appropriately. While not strictly on the subject of speech recognition, the paper explores the possibility of expanding this algorithm to include speech-to-text, which would be an added benefit for users that are in some way unable to type the commands necessary. 

### [Unmanned Aerial Vehicle Control](Unmanned_Aerial_Vehicle_Control.pdf)

[Original Link here](https://arxiv.org/abs/2009.04215i)
This paper explores the realm of voice commands to control unmanned vehicles, namely drones and the like. By being able to interpret speech commands, not only in English, but in Spanish as well, with different levels of distortion, the algorithm presents a unique opportunity to significantly expand the capabilities of remote control. Also utilizing a Hidden Markov Model, this speech-to-action algorithm could prove to be extremely useful as a starting point for our model as it is simultaneously able to extract voice from background noise.

### [Automatic Recognition of Lyrics in Singing](Automatic_Recognition_of_Lyrics.pdf)

[Original Link here](https://asmp-eurasipjournals.springeropen.com/articles/10.1155/2010/546047)
This paper looks at a system targeted towards recognizing phonemes and words from singing input. The network created by Mesaros and Virtanen also utilizes a Hidden Markov Model as a phonetic recognizer, wher the probability density function of each of the HMM states is modeled by a Gaussian mixture model. One benefit of this approach is that the acoustic system can be trained to interpret linguistic information to create more complex multilingual models. This information could prove useful in application to our project as it demonstrates the breakdown of language into its three classes of sounds- vowels, consonants, and nonspeech- and further elaborates on how each subpart should be approached. 

### [Automatic Lyrics Transcription using Dilated CNNs](Automatic_Lyrics_Transcription.pdf)

[Original Link here](https://arxiv.org/pdf/2007.06486.pdf)
In this paper, Demirel et al. propose a model for lyric transcription that utilizes convolutional time-delay networks. Tested exclusively on English lyrics in the DAMP-Sing! dataset, the network is trained on monophonic Karaoke recordings of pop songs over 150 hours of trainable data. Available at https://github.com/emirdemirel/ALTA, this dataset could prove useful to our research by providing a base pipeline from which we can build our network.

##Datasets

