# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 23:49:20 2025

@author: priya
"""

def countVowels(s):
    set1 = {'a','e','i','o','u'}
    count = 0
    for i in s:
        if i in set1:
            count += 1
            
    return count
        

print(countVowels("priyamou"))