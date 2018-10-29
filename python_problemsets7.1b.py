#/usr/bin/env python3


#write a script to write the of output of  the contents of 7.1 to a new file]

import re

infile  =  open("Python_07_nobody.txt","r")
outfile = open("nobody.txt",'w')

#print("line_number","start_position","end_position", sep = '\t')
outfile.write("line_number\tstart_position\tend_position\n")

line_counter = 0

for line in infile:
    line = line.rstrip()
    line_counter += 1
    for found in re.finditer(r"Nobody", line):
        nobody_start = found.start() + 1
        nobody_end = found.end() + 1
        #print(line_counter,nobody_start, nobody_end, sep='\t')
        string = '{}\t{}\t{}' 
        new_string =string.format(line_counter,nobody_start, nobody_end) 
        outfile.write(new_string + "\n")

infile.close()
outfile.close()





