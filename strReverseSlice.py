# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:28:44 2021

@author: priya
"""

def strReverseSlice1(s):
    return s[len(s)-1:len(s)//2:-1]

print(strReverseSlice1("PriyamRao"))