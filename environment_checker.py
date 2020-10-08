try: 
    import matplotlib
except:
    print("The following package is not installed: " , "matplotlib = 2.0.2")

try: 
    import tqdm
except:
    print("The following package is not installed: " , "tqdm")
    
try: 
    import tensorflow
except:
    print("The following package is not installed: " , "tensorflow = 2.0")
 
try: 
    import pandas
except:
    print("The following package is not installed: " , "pandas")
 
try: 
    import opencv
except:
    print("The following package is not installed: " , "opencv")
    
try: 
    import skimage
except:
    print("The following package is not installed: " , "skimage")

try: 
    import sys
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
    

if tensorflow.__version__ != "2.0":
    print("check tensorflow version")
if matplotlib.__version__ != "2.0.2":
    print("Check matplotlib version")
if pandas.__version__ == "0":
    print("Check pandas version")
if opencv.__version__ == "0":
    print("Check opencv version")
if skimage.__version__ == "0":
    print("Check scikit-image version")
if sys.version.split(" ")[0] != '3.8':
    print("Check pandas version")
if tqdm.__version__ == "0":
    print("Check pandas version")
else:
    print("Environment is Setup Correctly")




