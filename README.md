# 2020-Speech-Recognition



### Directory Guide

| File                        | Description                                                                                                           |
| -------------               | -------------                                                                                                         |
| environment.yml             | Contains dependencies to create a new virtual environment from.                                                       |
| environment_checker.py      | Installs necessary packages and checks that versions are up to date.                                                  |
| data_checker.py             | Checks for dataset in directory and provides download options otherwise.                                              |
| DataGenerator.py            | Generates data in batches for training given a path to training data, provides method to extract individual batches.  |
| DataAugmentation.py         | Performs different types of augmentation on data, including injecting noise and changing speed.                       |
| Data_Visualization.ipynb    | Provides visualizations of audio data using mel spectograms and tempo estimation, among other methods.                |
| input_pipeline.ipynb        | Creates TF.data dataset from audio data and provides parallelizations for optimization.                               |

### Testing the Model

You can run the following Google Colab notebook that walks through the process behind our model and provides the option to upload a file and test it out:

https://colab.research.google.com/drive/1e-qTOuuntbBJlDb5v8JPLPOqTqZzYJ30?authuser=1#scrollTo=BbpzxVg0iUsH

### Product Demonstration

Feel free to take a look at the following video from our presentation at the FIRE Research Summit 2020:

https://www.youtube.com/watch?v=2-uc0R6Kx_o





























