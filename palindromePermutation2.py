# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 20:27:29 2022

@author: priya
"""

def palindromePermutation(s):
    check = 0
    for i in s:
        a = s.count(i)
        if a%2!=0:
            check += 1
    if check>1:
        return False
    else:
        return True
    
    
print(palindromePermutation("abcabd"))