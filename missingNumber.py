# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 22:38:37 2023

@author: priya
"""

def missingNumber(n, givenSum):
    return int(n*(n+1)/2) - givenSum

print(missingNumber(100,5023))