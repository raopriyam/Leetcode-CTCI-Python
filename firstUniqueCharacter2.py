# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:49:08 2021

@author: priya
"""

def firstUniqueCharacter(s):
    dict1 = {}
    for i in s:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    print(dict1)
    for i in dict1:
        if dict1[i] == 1:
            return s.index(str(i))-1

print(firstUniqueCharacter("priyamiraop"))

