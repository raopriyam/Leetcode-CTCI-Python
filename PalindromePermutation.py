# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:27:15 2021

@author: priya
"""

def pal_permutation(s):
    oneval = 0
    dict1 = {}
    for i in s:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for key in dict1:
        #print(key)
        if int(dict1[key]%2) == 1:
            oneval += 1 
        #print(dict1[key])
    #print(oneval)
    if oneval <= 1:
        return True
    else:
        return False
        
   
        
        
print(pal_permutation("PRIYAM"))
print(pal_permutation("tactcoapapa"))