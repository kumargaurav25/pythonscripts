import sys
import os

listdir = sys.argv[1]
print(os.getcwd())
filelist = []

for root, dirs, files in os.walk(listdir):
    for file in files:
        filelist.append(os.path.join(root, file))

for name in filelist:
    print(name)