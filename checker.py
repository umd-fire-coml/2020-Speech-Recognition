import argparse, os
from argparse import ArgumentParser

parser = argparse.ArgumentParser(description = 'Dataset Checker')
parser.add_argument('folder', type = str, help = 'Folder to Check for')
args = parser.parse_args()

folder = args.folder

if (os.path.exists(folder) and os.listdir(folder)):
    print("Data exists on the current path.")
else:
    print("Data does not exist on the current path.")
