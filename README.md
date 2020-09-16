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

