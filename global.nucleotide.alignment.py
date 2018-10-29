#!/usr/bin/env python3

#write a simple global nt alignment program of your own sequences



sequence1 = 'agtctgtca'

sequence2 = 'gatctctgc'


#creating the reverse complement







for nt in range(len(sequence1)): 
    if sequence1[nt] == sequence2[nt]:
        print("position", nt ,"is a match")

    else:
        print("position", nt ,"is not a match")
