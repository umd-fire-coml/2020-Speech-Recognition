try: 
    import matplotlib
except:
    print("The following package is not installed: " , "matplotlib = 2.0.2")
    if matplotlib.__version__ != "2.0.2":
        print("Check matplotlib version")
        
try: 
    import tqdm
except:
    print("The following package is not installed: " , "tqdm")
      if tqdm.__version__ == "0":
        print("Check tqdm version")
    
try: 
    import tensorflow
except:
    print("The following package is not installed: " , "tensorflow = 2.0")
    if tensorflow.__version__ != "2.0":
        print("check tensorflow version")
 
try: 
    import pandas
except:
    print("The following package is not installed: " , "pandas")
    if pandas.__version__ == "0":
        print("Check pandas version")
 
try: 
    import opencv
except:
    print("The following package is not installed: " , "opencv")
    if opencv.__version__ == "0":
        print("Check opencv version")
    
try: 
    import skimage
except:
    print("The following package is not installed: " , "skimage")
    if skimage.__version__ == "0":
        print("Check scikit-image version")

try: 
    import sys
except:
    print("The following package is not installed: " , "sys = 3.8")
    if sys.version.split(" ")[0] != '3.8':
        print("Check sys version")
    
try:
    import numpy
 except: 
    print("The following package is not installed: " , "numpy")
 
try:
    import librosa
except:
    print("The following package is not installed: " , "librosa")
  
