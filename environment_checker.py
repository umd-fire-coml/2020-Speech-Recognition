try: 
    import matplotlib
    if matplotlib.__version__ != "2.0.2":
        print("Check matplotlib version")
except:
    print("The following package is not installed: " , "matplotlib = 2.0.2")
    
        
try: 
    import tqdm
    if tqdm.__version__ == "0":
        print("Check tqdm version")
except:
    print("The following package is not installed: " , "tqdm")
      
    
try: 
    import tensorflow
    if tensorflow.__version__ != "2.0":
        print("check tensorflow version")
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
    print("The following package is not installed: " , "skimage")
    

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
  
