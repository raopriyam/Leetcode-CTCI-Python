# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:54:20 2023

@author: priya
"""

def palindromeNumber(number):
    numCheck1 = str(number)
    numCheck2 = str(number)[::-1]
    if numCheck1 == numCheck2:
        return True
    return False

print(palindromeNumber(12342))
print(palindromeNumber(1234321))