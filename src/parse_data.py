#!/usr/bin/python

import fileinput
import sys
import re


with open("data/data.html", 'r', encoding='utf-8') as file:
	contents = file.read()

fileOut = open('data/data.txt', "w")

lined_contents = contents.split("\n")

string_for_printing = ""

for line in lined_contents:
	string_for_printing += line	

pattern = 'rgba(0, 0, 0, 0.4); }</style>'

# removes everything before match, including match
string_for_printing = string_for_printing.split(pattern, 1)[1]

pattern = '<div style="font-size:13px; margin-top:10px; padding-bottom:10px'

# removes everything after match, including match
string_for_printing = string_for_printing.split(pattern, 1)[0]

fileOut.write(string_for_printing)

