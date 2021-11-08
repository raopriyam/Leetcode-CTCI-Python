# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:24:48 2021

@author: priya
"""

def removeVowels2(s):
    s1 = ""
    set1 = {"a","A","e","E","i","I","o","O","u","U"}
    for i in s:
        if i not in set1:
            s1 = s1 + i
    return s1

print(removeVowels2("priyam"))