try: 
    import matplotlib
    if matplotlib.__version__ != "2.1.0":
        print("Ensure matplotlib version is 2.1.0")
except:
    print("The following package is not installed: " , "matplotlib = 2.1.0")
    
        
try: 
    import tqdm
    if tqdm.__version__ == "0":
        print("Check tqdm version")
except:
    print("The following package is not installed: " , "tqdm")
      
    
try: 
    import tensorflow
    if tensorflow.__version__ != "2.0":
        print("Ensure tensorflow version is 2.0.*")
    try:
        from tensorflow import keras
        if keras.__version__ != "2.0":
            print("Ensure keras version is 2.0.*")
    except:
        print("Error importing keras modules")
except:
    print("The following package is not installed: " , "tensorflow = 2.0")
   
 
try: 
    import pandas
    if pandas.__version__ == "0":
        print("Check pandas version")
except:
    print("The following package is not installed: " , "pandas")
    
 
try: 
    import opencv
    if opencv.__version__ == "0":
        print("Check opencv version")
except:
    print("The following package is not installed: " , "opencv")
    
    
try: 
    import skimage
    if skimage.__version__ == "0":
        print("Check scikit-image version")
except:
    print("The following package is not installed: " , "scikit-image")
    

try:
    import sklearn
    if sklearn.__version__ == "0":
        print("Check scikit-learn version")
except:
    print("The following package is not installed: " , "scikit-learn")


try: 
    import sys
    if sys.version.split(" ")[0] != '3.8':
        print("Check sys version")
except:
    print("The following package is not installed: " , "sys = 3.8")
    
    
try:
    import numpy
 except: 
    print("The following package is not installed: " , "numpy")


try:
    import librosa
except:
    print("The following package is not installed: " , "librosa")


try:
    import ffmpeg
except:
    print("The following package is not installed: " , "ffmpeg")
