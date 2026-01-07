# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 23:46:09 2026

@author: priya
"""

vowels = {'a','e','i','o','u'}

def countVowels(s):
    counter = 0
    for i in s:
        if i in vowels: 
            counter += 1
            
    return counter 


print(countVowels("priyam"))
        