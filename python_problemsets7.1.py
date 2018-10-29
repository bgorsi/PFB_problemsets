#!/usr/bin/env python3

#write a script to find every occurence of 'Nobody" and print out the position

import re

infile  =  open("Python_07_nobody.txt","r")

print("line_number","start_position","end_position", sep = '\t')
line_counter = 0
for line in infile:
    line = line.rstrip()
    line_counter += 1
    for found in  re.finditer(r"Nobody", line):
        nobody_start = found.start() + 1
        nobody_end = found.end() + 1 
        print(line_counter,nobody_start, nobody_end, sep='\t')

