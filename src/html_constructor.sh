#!/bin/bash

filename="public/index.html"

cat html_pieces/0.html > $filename
cat data/data.txt >> $filename
cat html_pieces/1.html >> $filename



