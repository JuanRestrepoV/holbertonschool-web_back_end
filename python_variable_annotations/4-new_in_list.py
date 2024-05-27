#!/usr/bin/python3
"""def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return my_list
    
    if idx > len(my_list):
        return my_list
    
    new_list[idx] = element
    
    return new_list
"""

"""
import sys

string = "And that piece of art is useful - Dora Korpar, 2015-10-19"
sys.stderr.write(string)
exit(1)
"""
array = [2, 3, 4, 2, 6, 2, 5]
newArray = []

def gettingMaxNumber():
    cant = 3
    
    for exec in range(cant):
        for value in array:
            newArray.append(value)
        
    for maxNum in newArray:
        if maxNum[0] > maxNum[1] and maxNum[0] > maxNum[2]:
            print(maxNum[0])
        if maxNum[1] > maxNum[0] and maxNum[1] > maxNum[2]:
            print(maxNum[1])
        if maxNum[2] > maxNum[0] and maxNum[2] > maxNum[1]:
            print( maxNum[2])
    
    
