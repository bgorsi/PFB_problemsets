#!/usr/bin/env python3

#write a script in which you construct a dictionary of your favorite
#things


fav_dict = { 'book' : 'Jitterbug Perfume', 'song' : "Tom Petty-I won't Back Down",'tree' : 'Cedar ' }
print(fav_dict['book'])

fav_thing = 'book'
print(fav_dict[fav_thing])



print(fav_dict['tree'])

#add your favorite organism to the dictionary

fav_dict['organism'] = 'zebrafish'

fav_thing = 'organism'

print(fav_dict[fav_thing])


str = input("Enter your input: ");
print ("Received input is : ", str)



fav_dict['organism'] = 'chimpanzee'

print(fav_dict[fav_thing])

for i in fav_dict:
    value = fav_dict[i]
    print('key:', i, 'value:',value)


