import matplotlib,tqdm, tensorflow, pandas, opencv, skimage, sys


if tensorflow.__version__ != "2.0":
    print("check tensorflow version")
elif matplotlib.__version__ != "2.0.2":
    print("Check matplotlib version")
elif pandas.__version__ == "0":
    print("Check pandas version")
elif opencv.__version__ == "0":
    print("Check opencv version")
elif skimage.__version__ == "0":
    print("Check scikit-image version")
elif sys.version.split(" ")[0] == '3.7':
    print("Check pandas version")
elif tqdm.__version__ == "0":
    print("Check pandas version")
else:
    print("Environment is Setup Correctly")




