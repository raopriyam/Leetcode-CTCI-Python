# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:52:28 2023

@author: priya
"""

def isUnique(string):
    return len(set(string)) == len(string)

print(isUnique("Priyam"))