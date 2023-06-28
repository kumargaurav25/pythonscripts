import re
import sys


srchstr = sys.argv[1]
# Take the pattern or string as the first parameter
srchfile = sys.argv[2]
# Take the filename as second parameter

#print(srchstr)

inf = open(srchfile)
#Opening the file
for line in inf:
#Going line by line through the file
    if(re.search(srchstr, line)):
    # If the expression is found then print the whole line, or else move on.
        print(line)

inf.close()
#Closing the file.