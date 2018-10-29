#!/usr/bin/env python3
import sys 

number = int(sys.argv[1])

if number > 0:
    print ("positive")
    if number < 50:
        print ("smaller than 50")
        if number %2 ==0:
            print ("it is an even number that is smaller than 50")
    elif number > 50:
        print("greater than 50")
        if number %3 ==0:
            print ("it is larger than 50 and divisible by 3")
elif number == 0: 
    print ("zero")
else:
    print ("negative")

print("you're doing awesome!")



