#!/usr/bin/python
__author__ = 'riizade@gmail.com'

import sys

inputfile = sys.argv[1]
outputfile = sys.argv[1]
if len(sys.argv) == 3:
	outputfile = sys.argv[2]

infile = open(inputfile, "r")

sorted_lines = sorted(infile, key=str.lower)
infile.close()

outfile = open(outputfile, "w")
for line in sorted_lines:
    outfile.write(line)

outfile.close()