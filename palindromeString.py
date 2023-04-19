# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:52:05 2023

@author: priya
"""

def palindromeString(string):
    stringCheck = string[::-1] 
    if stringCheck == string:
        return True
    return False

print(palindromeString("priyam"))
print(palindromeString("priyamayirp"))