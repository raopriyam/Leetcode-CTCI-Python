# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:01:00 2023

@author: priya
"""

def palindromePermutationNumber1(n):
    return len(set(str(n))) == int(len(str(n))/2) + 1

print(palindromePermutationNumber1(123432))