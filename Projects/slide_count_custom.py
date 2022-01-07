import os
import sys
import zipfile
import re
import argparse

# Create an empty dictionary which contains the path of the pptx files path
# and the number of slides in the pptx file
collection_of_pptx_files = {}


parser = argparse.ArgumentParser(description='Slide Counter')

parser.add_argument('--path', type=str,
                    help='a path of the folder')
parser.add_argument('--summary', default=False, type=lambda x: (str(x).lower() == 'true'))

args = parser.parse_args()


root_dir = args.path
show_summary = args.summary

def get_pptx_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.pptx'):
                collection_of_pptx_files[os.path.join(root, file)] = 0

# called get_pptx_files
get_pptx_files(root_dir)
print(collection_of_pptx_files)

# (function) called get_slide_count
def get_slide_count(collection_of_pptx_files):
    for file in collection_of_pptx_files:
        try:
            archive = zipfile.ZipFile(file, 'r')
            contents = archive.namelist()
        except Exception as e:
            print("Error reading %s (%s). Count will be 0." % os.path.basename(file, e))
        else:
            for fileentry in contents:
                if re.search('ppt/slides/slide', fileentry):
                    collection_of_pptx_files[file] += 1
    return collection_of_pptx_files

# (function) called print_slide_count
def print_slide_count(collection_of_pptx_files):
    for file, count in sorted(collection_of_pptx_files.items(), key=lambda x: x[1], reverse=True):
        print("%s\t%s" % (count, os.path.basename(file)))





get_slide_count(collection_of_pptx_files)
print_slide_count(collection_of_pptx_files)


