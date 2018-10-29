#!usr/bin/env python3

#Create a function to format a string of DNA so that each line is no more than 60 nt long. Your function will

#NPUT: a string of DNA without newlines
#OUTPUT: a string of DNA with lines no more than 60 nucleoties long

import re 

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

#mod_nt_length = re.findall(r"(.{60})", dna)
#join_list = ('\n'.join(mod_nt_length) + '\n')
#print(join_list)


#create a function 

def join_list(dna):
    mod_nt_length = re.findall(r"(.{60})", dna)
    join_list = ('\n'.join(mod_nt_length) + '\n')
    return join_list

join_list(dna)

print("woohoo!")

