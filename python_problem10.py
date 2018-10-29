#!usr/bin/env python3

#create a DNA sequence class that will contain a sequence, its name, and its organism of origin. Do this by creating an _init_function





class DNAsequence(object):

#Dna sequences class should contain a sequence (attribute)
#dna sequence class should have a name (attribute)
#dna sequence class should have an organism of origin (attribute)
    dna_seq = 'atggtcgggttttcccaagtc'
    gene_name = 'new_gene'
    species_origin = "Danio rerio"
    
dnaseq_object =DNAsequence()

print(' I Bushra Gorsi created a record for ' + dnaseq_object.gene_name + ' from ' + dnaseq_object.species_origin)

print('This is the sequence for new gene ' + dnaseq_object.dna_seq)




