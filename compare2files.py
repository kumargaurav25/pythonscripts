import sys


def CompareFiles():
    file1 = open(sys.argv[1], 'r')
    file2 = open(sys.argv[2], 'r')
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
    for i in range(len(file1_lines)):
        if file1_lines[i] != file2_lines[i]:
            print("Line " + str(i + 1) + " doesn't match.")
            print("-----------------------------------")
            print("File1: " + file1_lines[i])
            print("File2: " + file2_lines[i])
    file1.close()
    file2.close()


i = 1
for i in range(1, len(sys.argv)):
    print('File ' + str(i) + ' is ' + sys.argv[i])
if i > 2:
    print("Can only compare 2files. Try again")
elif i < 2:
    print("Need 2 files to compare. Try again")
else:
    CompareFiles()
