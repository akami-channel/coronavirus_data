#!/usr/bin/python


import fileinput
import sys
import csv

# data_file = open('hopkins_data.csv', "r")
fileOut = open('public/data.js', "w")

results = ""
outputColNum = 0

counter = 0
rowNum = 0

fileOut.write("dataString = \"{")

with open('hopkins_data.csv', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    # reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results += "\'datarow" + str(rowNum) + "\'" + ": "
        results += str(row)
        results += ", "
        # if (rowNum == 1):
        # 	print(row)
        rowNum += 1
        # for colNum, val in enumerate(row):
        #     # YELLOW DIMENSIONS ARE FROM ROW=3 to ROW=12 ....... and COL=3 to COL=6
        #     if(rowNum == 2):
        #         # print(counter, rowNum, colNum, val)       
        #         # print(val)
        #         # print(str(val) + "," + str(rowNum) + "," + str(colNum))
        #         results += str(val)
        #         results += ","
        #         outputColNum += 1
        #     counter += 1
        # rowNum += 1

fileOut.write(results)
fileOut.write("}\";")
fileOut.write("\n")
