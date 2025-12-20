# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 22:51:35 2025

@author: priya
"""

def wordCheck(word):
    if word.isalpha():
        print("alphabates")
    elif word.isdigit():
        print("numbers")
    elif word.isalnum():
        print("alphabates and numbers")
    else:
        print("something else")
        
        
wordCheck("Priyam")