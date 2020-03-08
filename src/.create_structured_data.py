#!/usr/bin/python


import fileinput
import sys
import csv
import json

fileOut = open('public/data.JSON', "w")

results = ""
outputColNum = 0

counter = 0
rowNum = 0

fileOut.write("[")

with open('hopkins_data.csv', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    # reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        # Following line is just for outputting double quotes instead of single
        results += json.dumps(row)
        results += ", "
        rowNum += 1

# removing end of data because it has }, that I don't want
results = results[0:len(results) - 3]
results = results + "}]"

fileOut.write(results)
fileOut.write("\n")
