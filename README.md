# 2020-Speech-Recognition

* [Directory Guide](#directory-guide)
* [Product Demo](#product-demonstration)
* [How To Use The Data Checker](#how-to-use-the-data-checker)
  * [Adding a New Dataset](#adding-a-new-dataset)
  * [Updating a Existing Dataset](#updating-a-existing-dataset)
  * [Deleting an Existing Dataset](#deleting-an-existing-dataset)
  * [Using a Different Data Store](#using-a-different-data-store)
* [Training New Models](#training-models)
* [Testing New Models](#testing-models)

## Directory Guide

| File                        | Description                                                                                                           |
| -------------               | -------------                                                                                                         |
| environment.yml             | Contains dependencies to create a new virtual environment from.                                                       |
| environment_checker.py      | Installs necessary packages and checks that versions are up to date.                                                  |
| data_checker.py             | Checks for dataset in directory and provides download options otherwise.                                              |
| DataGenerator.py            | Generates data in batches for training given a path to training data, provides method to extract individual batches.  |
| DataAugmentation.py         | Performs different types of augmentation on data, including injecting noise and changing speed.                       |
| Data_Visualization.ipynb    | Provides visualizations of audio data using mel spectograms and tempo estimation, among other methods.                |
| input_pipeline.ipynb        | Creates TF.data dataset from audio data and provides parallelizations for optimization.                               |

### Product Demonstration

Feel free to take a look at the following video from our presentation at the FIRE Research Summit 2020:

[![FIRE Research Summit 2020 Submission Video](https://img.youtube.com/vi/2-uc0R6Kx_o/0.jpg)](https://www.youtube.com/watch?v=2-uc0R6Kx_o)

You can also run the following Google Colab notebook that walks through the process behind our model and provides the option to upload a file and test it out:

[FIRE Research Summit 2020 Submission Notebook](https://colab.research.google.com/drive/1e-qTOuuntbBJlDb5v8JPLPOqTqZzYJ30?authuser=1#scrollTo=BbpzxVg0iUsH)


## How To Use The Data Checker

Using the Data Checker with the default dataset is very easy. Simply run,

```bash
python3 data_checker.py
```

and the Data Checker will check if the default dataset exists, and if it does not, it will download this dataset, expand it, and move it to its intended location.

### Adding a New Dataset

To add and download a new dataset, you must specify run the data\_checker.py file with four command line arguments:

```bash
python3 data_checker.py -n name_of_your_dataset -u download_url_of_your_dataset -f local_directory_for_your_dataset -t file_type
```

The current explicitly supported file types are zip and tar.gz. If none of these file types are given, your data will still be downloaded and moved to the correct directory, but it will not be expanded if it is in a compressed format.

### Updating a Existing Dataset

If you want to update an existing dataset, you must specify the same command line arguments as adding a new dataset and add a "-a update" flag.

```bash
python3 data_checker.py -n name_of_dataset_to_update -u new_url -f new_local_directory -t new_file_type -a update
```

Updating a dataset is equivalent to deleting a dataset and adding a new dataset with the modified parameters. This function will update AND download a new veersion of the dataset. If you only want to delete, please use the delete function below.

### Deleting an Existing Dataset

If you want to delete an existing dataset, you must specify the name of the dataset you wish to delete and add a "-a delete" flag.

```bash
python3 data_checker.py -n name_of_dataset_to_delete -a delete
```

### Using a Different Data Store

If there ever arises the need to have multiple data stores (in our case csv files with metadata about each dataset), you can use the -d flag to specify a new data store file. This will also create a new data store if one does not already exist at that location. 

```bash
python3 data_checker.py -d data_store_file [...and any other command line arguments you may need...]
``` 

## Training Models

The [Train_Model](Model/Train_Model.ipynb) notebook details how to train our Speech To Text model. To run the notebook, make sure you have placed this repository in the "Research/FIRE/" folder on your Google Drive. There are two datasets that you can train on within this notebook: Common Voice and Amazing Grace. 

If you try to download the Common Voice dataset on Google Colab, Google Colab will crash. To circumvent this issue we had placed the tfrecords of the train subset on Google Drive in the data directory. The cells on the training notebook will use use those tfrecords from the data directory. 

If you would like to use the Amazing Grace dataset, follow the instructions [above](#how-to-use-the-data-checker) to obtain the Amazing Grace dataset. The training notebook uses the DataGenerator to generate data for training. You can modify the training parameters to fit the data to your choosing. 

The results can be visualized using Tensorboard

## Testing Models

The [Test Model](Test_Model.ipynb) notebook details how to test our Speech To Text model. To run the notebook, make sure you have placed this repository in the "Research/FIRE/" folder on your Google Drive. You can select which pre-trained model you want to test by changing the argument for:

```
compiled_model.load_weights(your_pretrained_model_here)
```

Once you have chosen your pre-trained model, you can change the files array with a list of all the audio files you want use to test your model:

```
files = ["example.mp3"]
```


