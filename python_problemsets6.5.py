#!/usr/bin/env python3

#will input three seperate files, open each file and add geneIDs to a set. one Set per file
#A) find all the genes that are not cell proliferation genes.
#B)Find all genes that are both stem cell proliferation genes and pigment genes


infile1 = open ("alpaca_all_genes.txt" , "r" )
infile2 = open ("alpaca_stemcellproliferation_genes.txt" , "r")
infile3 = open ("alpaca_pigmentation_genes.txt" , "r")
outfile1= open ("genes_not_proliferation.txt", "w")
outfile2= open ("both_stem_and_pigment.txt" , "w")

list1= []

for line in infile1:
    line = line.rstrip()
#   set1.add(str(line))
    if 'Gene stable ID' in line:
        continue
    list1.append(line)

set1 = set(list1)
print(set1)



list2= []
for line in infile2:
    line = line.rstrip()
    if 'Gene stable ID' in line:
        continue
    list2.append(line)

set2 = set(list2)

list3 = []
for line in infile3:
    line = line.rstrip()
    if 'Gene stable ID' in line:
        continue
    list3.append(line)

set3 = set(list3)

prolif_minus_genes = set1 - set2

intersect_genes = set2 & set3


list_prolif = list(prolif_minus_genes)
list_intersect = list(intersect_genes)





outfile1.write('\n'.join(list_prolif) + '\n')
outfile2.write('\n'.join( list_intersect) + '\n')

infile1.close()
infile2.close()
infile3.close()
outfile1.close()
outfile2.close()
