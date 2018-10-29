#!/usr/bin/env python3


#write a script to do the following: open and read the contents, uppercase each line, print each line to STDOUT


file_object = open("Python_06.txt", "r")
song_re_wrote = open("Python_06_uc.txt", "w")    #writing to a new file once modified
for line in file_object:
    stripped_line = line.rstrip()       #always do this when reading a file to remove newline characters
    upper_stripped_line = stripped_line.upper()  #convert each line to uppercase
    #print(upper_stripped_line)    #commented out so can run problem 6.2
    song_re_wrote.write(str(upper_stripped_line) + "\n")  #writes everyline to the new file and adds newline) 
    

file_object.close()
song_re_wrote.close()

print("Wrote 'Python_06_uc.txt'")
