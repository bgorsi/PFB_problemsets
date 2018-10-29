#!/usr/bin/env python3



#Do the same as above but do it by creating an init function:
#functions have to be defined and attributes dont have as return function as just are variables that become methods in a class.

class DNAnewsequence(object):
    def _init_ (self, dna_seq, gene_name, species_origin):
        self.dna_seq= dna_seq
        self.gene_name = gene_name
        self.species_origin = species_origin
            
#dna_seqobject2 = DNAnewsequence('atggtcgggttttcccaagtc', 'new_gene','Danio rerio')
dna_seqobject2 = DNAnewsequence()

print('name:' , gene_name, 'has the sequence', dna_seq , 'from the organism', species_origin)
    
