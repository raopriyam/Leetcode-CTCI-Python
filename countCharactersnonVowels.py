# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 23:50:01 2026

@author: priya
"""

vowels = {'a','e','i','o','u'}

def countcharacternonvowels(s):
    counter = 0
    for i in s:
        if i in vowels: 
            counter += 1
            
    return len(s) - counter 


print(countcharacternonvowels("priyam"))
        