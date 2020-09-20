# 2020-Speech-Recognition

Gender Recognition
Study: http://athena.csus.edu/~makwanap/FinalReport.pdf
Dataset: https://www.kaggle.com/primaryobjects/voicegender
CSV file with frequency attributes from converting sound waves for both genders
Uses:
Identifying human sounds (e.g. “This is a male laughing”) or other uses
Categorizing audios/videos according to preferences 
Greetings  
“Can help personal assistants like Siri, Google Assistant to answer the question with female generic or male generic results.”
Difficult to define and also controversial!


Language Detection
https://www.kaggle.com/toponowicz/spoken-language-identification
Only English, German, Spanish, French data available here
https://github.com/tomasz-oponowicz/spoken_language_identification
Big variance forces the model to concentrate more on language properties as opposed to a specific voice.
Each sample is an FLAC audio file with:
sample rate: 22050
bit depth: 16
channels: 1
duration: 10 seconds (sharp)
The original recordings are MP3 files but they are converted into FLAC files quickly

# Research

Text overlay and subtitle generation. Aim to transcribe an audio or video file and in multiple languages through reliable and fast methods

## Information and method: 

The process for transcription is time consuming and requires a lot of educated people with language profciency. This effort is compounded when a multi-language 
transcript is required. Natural language processing (NLP) and translation are some of the hardest problems for computers to solve because of the many idiomatic elements
of speech. This requires a native speaker of both the source and target language to perform a translation. 
The recently introduced neural-network based approach to machine translation has brought on unprecedented translation 
accuracy and fluency. While it is not perfect yet, it is now a viable solution for many more use cases than ever before.

* Step 1: Recognise Speech in audio or video files.
* Step 2: Storing the output in JSON file that includes word-level time stamping, punctiation and confidence levels.
* Step 3: Converting to relevant sub title file format. For example .SRT file.
* Step 4: Overlaying it on video or audio files with media player or online tools. 

Other steps may include language conversion using Neural Machine Translation[NMT].

## References:
https://aws.amazon.com/blogs/machine-learning/create-video-subtitles-with-translation-using-machine-learning/
https://paperswithcode.com/paper/covost-2-a-massively-multilingual-speech-to
https://paperswithcode.com/paper/mel-spectrogram-augmentation-for-sequence-to
