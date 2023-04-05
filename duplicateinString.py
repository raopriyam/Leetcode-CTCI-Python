# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:55:59 2023

@author: priya
"""

def duplicateStringCharacters(string):
    dict1 = {}
    for i in string:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1


print(duplicateStringCharacters("priyam rao"))