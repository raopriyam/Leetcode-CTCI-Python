# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:33:53 2023

@author: priya
"""

def palindromePermutationString1(string):
    string = string.replace(" ","")
    string = string.lower()
    
    set1 = set(string)
    if len(set1) == int(len(string)/2) + 1:
        return True
    return False
    
     

print(palindromePermutation("ayakk"))