#!/usr/bin/env Python3

#take a multi fasta file from user input and calculate the nucleotide composition for each. Create a datastructure to keep count. Print out each sequence name and its composition


#- create an empty dictionary to store the key value pairs
#- parse the fasta file by name and sequence 

import re

infile = open("Python_06.fasta", "r")

dictionary = {}
dictionary2 ={}
#gene_name = ''


#parse fasta file to create first dict

for line in infile:
    line = line.rstrip()
    if line.startswith('>'):
        remove_charac = line[1:]
        header_split = remove_charac.split(' ')
        gene_name = header_split[0]
        dictionary[gene_name] = '' 
    else: 
        sequence = line 
        #if gene_name in dictionary:
        dictionary[gene_name] += sequence  #appends sequence to gene name

#print(dictionary)

for gene_name in dictionary:
    sequence = dictionary[gene_name] #getting a value out of a gene name
    count_seq = len(sequence)
    a_count = sequence.count('A') / count_seq
    c_count = sequence.count('C') / count_seq
    g_count = sequence.count('G') / count_seq
    t_count = sequence.count('T') / count_seq
    dictionary2[gene_name]= {'A':a_count,'C':c_count,'G':g_count,'T':t_count}

print(dictionary2)
#print(a_count, c_count, g_count, t_count)


#calculate nucleotide composition
#for gene_name in dictionary:

#a_count = sequence.count('A') / count_seq 
#c_count = sequence.count('C') / count_seq
#g_count = sequence.count('G') / count_seq
#t_count = sequence.count('T') / count_seq
#print(a_count, c_count, g_count, t_count)

    


   #nt_count = len(line)
   #print(nt_count)

















#print (dictionary)
       




