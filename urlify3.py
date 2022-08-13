# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:46:58 2022

@author: priya
"""

def urlify3(s):
    s = s.split(" ")
    res = "" 
    for i in s:
        res = res + i + "%20" 
    return res

print(urlify3("priyam rao is my name"))
        
        