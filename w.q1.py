#!/usr/bin/env python3

infile = open ("human_cds.fasta" , "r")



dictionary ={}
current_id =""
dictionary2 ={}



for line in infile:
    if line.startswith(">"):
        line = line.rstrip("\n\n")
        line_rem_greater = line[1:]
        line_split = line_rem_greater.split(' ')
        current_id= line_split[0]

    else:
        sequence = line 
        if current_id in dictionary:
            dictionary[current_id] += sequence
        else:
            dictionary[current_id] = sequence

#print(dictionary)
for sequence_id in dictionary:
    count_len = (len(dictionary[sequence_id]))
    #print(len(dictionary[sequence_id]))
    #print(sequence_id)
    dictionary2[sequence_id] = count_len

print(dictionary2)


#creating a new dictionary with sequence id and count 


