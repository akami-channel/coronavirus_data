#!/usr/bin/python

import fileinput
import sys
import re

fileOut = open('data/data.txt', "w")

with open("data/data.html", 'r', encoding='utf-8') as file:
	contents = file.read()

lined_contents = contents.split("\n")

pattern1 = re.compile(r'^.*$')

num_matches = 0
print_all_switch = False
string_to_print = ""
the_rest_of_the_file = ""

for line in lined_contents:
	# file_single.write(line)
	if re.search(r'^.*main_table_countries_div.*$', line): # only matches if there is a "<"
		num_matches += 1
		if(num_matches == 2):
			print_all_switch = True
			fileOut.write(line + "\n")
	elif print_all_switch == True:
		the_rest_of_the_file += line
		# bla = re.search(r'^(.*)\[(.*)\](.*)$', line)
		# bla = re.search(r'^(.*)\[(.*)\].*\((.*)\)(.*)$', line)
		# I may have made this a little more complex than necessary bc I was trying \ instead of / as in the edict data
		#
		# bla = re.search(r'^(.*)\[(.*)\][^)]*\)(.*)$', line)
		#
		# string_to_hash = bla.group(1).strip() + "|" + bla.group(2)


pattern = "<div style=\"font-size:13px; margin-top:10px; padding-bottom:10px "

fileOut.write(the_rest_of_the_file.split(pattern, 1)[0])
