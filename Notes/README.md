# Research

This folder contains research papers we have read and notes
## Papers

### [Survey on Deep Neural Networks in Speech and Vision Systems](Survey_on_Deep_Neural_Networks_in_Speech_and_Vision_Systems.pdf)

[Original Link Here](https://arxiv.org/abs/1908.07656)
This paper surveys various DNNs for Speech and Vision applications. Alam et al. list and describe various techniques that have been recently employed for deep neural networks. For the purpose of our project, they list several models that would be worth exploring; Section 2.6 on Generative Models For Speech, 2.7 on Recurrent Neural Networks and LSTMs, and 2.8 on Attention Neural Networks seem to be the most relevant. The discussion in Section 3.2 covers these models in a little more depth and lists many papers and models that we could refer to in future research. This paper also surveys models that have resource constraints and are made to be more lightweight; although this seems to be outside the scope of our current research, it could be worth considering in the future. 

### [A Neural Conversational Model](A_Neural_Conversational_Model)

[Original Link Here](https://arxiv.org/abs/1506.05869)
This paper proposed a novel conversational model that was based on the Seq2Seq model. The researchers used the seq2seq framework to predict the next sentence given the previous sentence or sentences in a conversation. They showed that their model was able to hold simple conversation with detailed responses when given a dataset of an IT Helpdesk, and less detailed but mostly logically correct responses when shown a more open-domain dataset of movie transcripts.

### [Neural Approaches to Conversational AI](Neural_Approaches_to_Conversational_AI.pdf)

[Original Link Here](https://arxiv.org/abs/1809.08267)
This paper is a very extensive study and summary of using Neural Networks for Coversational AI. It is 95 pages long and has not been read extensively, but it may prove to be useful in the future if we choose to go along this path.

### [On the Correlation and Transferability of Features between Automatic Speech Recognition and Speech Emotion Recognition](On_the_Correlation_and_Transferability_of_Features_between_Automatic_Speech_Recognition_and_Speech_Emotion_Recognition.pdf)

[Original Link Here](https://pdfs.semanticscholar.org/9b32/4a985a3ab539045d09ec9419aef956cbaff8.pdf)
This paper took an interesting approach of comparing how tranferable ASR and SER models were. Rather than proposing any novel models per say, this study used the base layers of one model with the output layers of the other model to see if their was a significant decrease in model accuracy. What they found was that importing base layers from one model to another did not have a huge impact on performance. Through this study they showed the that low-level information for both ASR and SER models may be correlated. The models that this specific paper used were Convolutional Neural Networks. 

### [Real-Time Speech Emotion and Sentiment Recognition for Interactive Dialogue Systems](Real-Time_Speech_Emotion_and_Sentiment_Recognition_for_Interactive_Dialogue_Systems.pdf)

[Original Link Here](https://www.aclweb.org/anthology/D16-1110.pdf)
This paper proposed an approach of using a CNN model to extract emotion from raw speech input and was able to acheive an average 65.7% accuracy across 6 emotion/sentiment classes. Their CNN model required only a single filter which allowed it to obtain real-time performance.  

### [Evaluating deep learning architectures for Speech Emotion Recognition](Evaluating_deep_learning_architectures_for_Speech_Emotion_Recognition.pdf)

[Original Link Here](https://www.sciencedirect.com/science/article/abs/pii/S089360801730059X)
This paper evaluated various techniques for Speech Emotion Recognition using deep learning techniques. They used various RNN/LSTM and CNN models and compared their performance on the IEMOCAP dataset. They also employed different models for turn-based processing and frame-based processing. Turn-based processing attatched a label to each utterance whereas frame-based processing attatched a label to each frame. Their results showed the superiority of frame-based CNN models, but even this paper's accuracy was the state-of-the-art at the time of only 60-65% on their test datasets.

### [Hate me, hate me not: Hate speech detection on Facebook](Hate_me_hate_me_not_Hate_speech_detection_on_Facebook.pdf)

[Original Link Here](https://www.semanticscholar.org/paper/Hate-Me%2C-Hate-Me-Not%3A-Hate-Speech-Detection-on-Vigna-Cimino/2d21ebb96a5cd93bdfda391c70a3f77717b09833)
This paper used two techniques for Hate Speech detection using machine learning. The authors used LSTMs and SVMs to classify content on facebook as hate speech. They collected their own dataset on a subset of the data available on Facebook to target only Italian posts that consisted of 17567 comments and 99 posts. They also preprocessed their data with sentiment polarity and word embedding lexicons to improve the accuracy of their model. Overall, the LSTM outperformed the SVM with an accuracy of approximately 75% as compared to an accuracy of 73%. In comparision to the results of emotion detection from other papers, this approach of hate speech detection did seem to have more promising results. 

### [Using Convolutional Neural Networks to Classify Hate-Speech](Using_Convolutional_Neural_Networks_to_Classify_Hate-Speech.pdf)

[Original Link Here](https://www.researchgate.net/publication/318741626_Using_Convolutional_Neural_Networks_to_Classify_Hate-Speech)
This paper used CNNs for Hate Speech Discrimination. They divided their labels into 4 classes: sexism, racism, both, and non-hate speech. Notably despite their imbalanced dataset, their approach was able to obtain a precision of 86.61% on a dataset of a dataset of tweets. This paper also discussed the continious-bag-of-words and skip-gram models which may prove useful if we need to embed words for our own project. This result is definetly even more promising than the hate speech detection model discussed in the previous paper, but these models were trained on different datasets so it would be interesting to first check their performance by validating these models on each other's dataset and then comparing the results. 

## Datasets

* IT Helpdesk Dataset
* Movie Transcripts
* [TIMIT](https://deepai.org/dataset/timit) Acoustic-Phonetic Continuous Speech Corpus
* [IEMOCAP](https://sail.usc.edu/iemocap/) Interactive Emotional Dyadic Motion Capture
* Twitter
* Facebook
