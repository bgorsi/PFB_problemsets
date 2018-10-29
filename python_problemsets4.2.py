#usr/bin/env python3 

#write a script that splits a string into a list 


species = ('sapiens,erectus,neanderthelensis')
print (species)

split_species = species.split(',')
print(split_species)

sort_split_species = sorted(split_species)
print (sort_split_species)


sort_short_split_species = sorted(sort_split_species, key = len, reverse = True)
print(sort_short_split_species)

