#!/usr/bin/env python 3 

#write a script to parse the fasta file to a dicitonary 

import re

infile = open ("human_cds.fasta")

dictionary = {}

sequence= ''
header=''
count = 0 

for line in infile:
    line = line.rstrip()
    matches_header = re.search(r"^>" , line)
    if matches_header:
        header = line
        if len(sequence) > 0:
            dictionary[header] = sequence
        seq = ''
    else:
        sequence += line
dictionary[header] = sequence

print(dictionary)

#count the frequency of each nucleotide in the file






