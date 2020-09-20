import argparse, os
from argparse import ArgumentParser
import pandas as pd
import pickle
import sys

parser = argparse.ArgumentParser(description = 'Dataset Checker')
parser.add_argument('-d', '--dataframe', type = str, help = "Location of CSV Dataframe", default='.data-store.pkl')
parser.add_argument('-n', '--name', type = str, help='dataset to check for')
parser.add_argument('-u', '--url', type = str, help='dataset download link')
parser.add_argument('-f', '--folder', type = str, help = 'Folder to Check for')
args = parser.parse_args()

if os.path.exists(args.dataframe):
	df = pd.read_pickle(args.dataframe)
else:
	df = pd.DataFrame({"Name": [], "Folder": [], "URL": []})
	df = df.set_index("Name") 

if args.name not in df.index:
	if args.folder == None or args.url == None:
		print("Dataest not in data store. Please specify a folder location and a url for this dataset")
		sys.exit(0)
	df.loc[args.name] = [args.folder, args.url]
	df.to_pickle(args.dataframe) 

folder = df.loc[args.name]["Folder"]
url = df.loc[args.name]["URL"]

if (os.path.exists(folder) and os.listdir(folder)):
    print("Data exists on the current path.")
else:
    print("Data does not exist on the current path.")
    os.system("wget '%s'" % (url,))
    print("Downloaded dataset to current directory.\nPlease expand and move to directory %s as needed" % (folder,))
