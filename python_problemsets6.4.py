#!/usr/bin/env Python 

#write a script that opens a fastq file and go through each line of the file. Count the number of lines and thenumber of characters per line. have your script report the total number of lines , total number of characters perline and average line length



my_fastq = open("Python_06.fastq","r")

total_line_count = 0
line_charac_count = 0


for line in my_fastq:
    line = line.rstrip()
    line_charac_count += len(line)
    total_line_count  += 1   #add to the total line count 
    

print(line_charac_count)
print(total_line_count)

average_line_count = (line_charac_count / total_line_count)

print( average_line_count)
    


