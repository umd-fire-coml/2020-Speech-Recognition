import argparse, os
from argparse import ArgumentParser
import pandas as pd
import sys

parser = argparse.ArgumentParser(description = 'Dataset Checker')
parser.add_argument('-d', '--dataframe', type = str, help = "Location of CSV Dataframe", default='.data-store.csv')
parser.add_argument('-n', '--name', type = str, help='dataset to check for', default='smule')
parser.add_argument('-u', '--url', type = str, help='dataset download link')
parser.add_argument('-f', '--folder', type = str, help = 'Folder to Check for')
parser.add_argument('-a', '--action', type=str, help='action to take add/update/delete', default='add')
parser.add_argument('-t', '--type', type=str, help='Type of downloaded file', default="")
args = parser.parse_args()

if os.path.exists(args.dataframe):
	df = pd.read_csv(args.dataframe)
	df = df.set_index("Name")
else:
	df = pd.DataFrame({"Name": [], "Folder": [], "URL": [], "Type":[]})
	df = df.set_index("Name") 

if args.name not in df.index or args.action == "update":
	if args.folder == None or args.url == None:
		print("Dataest not in data store. Please specify a folder location and a url for this dataset")
		sys.exit(0)
	df.loc[args.name] = [args.folder, args.url, args.type]
	df.to_csv(args.dataframe) 

if args.name in df.index and args.action == "delete":
	df = df.drop(args.name)
	df.to_csv(args.dataframe)
	print("Deleted %s dataset" % (args.name,))
	sys.exit(0)

folder = df.loc[args.name]["Folder"]
url = df.loc[args.name]["URL"]
typ = df.loc[args.name]["Type"]

if (os.path.exists(folder) and os.listdir(folder)):
    print("Data exists on the current path.")
else:
	print("Data does not exist on the current path.")
	os.system("wget '%s'" % (url,))
	print("Downloaded dataset to current directory.")
	os.system("mkdir -p '%s'" % (folder,))

	if typ == "zip":
		os.system("unzip '%s' -d '%s'" % (os.path.basename(url), folder))
		print("Unzipped '%s' to '%s'" % (os.path.basename(url), folder))
	elif typ == "tar.gz":
		os.system("tar -xvzf '%s' -C '%s'" % (os.path.basename(url), folder))
		print("Expanded '%s' to '%s'" % (os.path.basename(url), folder))
	else:
		os.system("mv '%s' '%s'" % (os.path.basename(url), folder))
		print("Moved '%s' to '%s'" % (os.path.basename(url), folder))
	
	if typ == "zip" or typ == "tar.gz":
		os.system("rm %s" % (os.path.basename(url),))
		print("Removed expanded file") 
		
