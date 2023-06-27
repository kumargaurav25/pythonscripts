import csv
import sys

filename=sys.argv[1]
with open(filename, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    for row in csvreader:
        print(row[1])

