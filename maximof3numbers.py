# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 23:41:27 2026

@author: priya
"""

def maxin3numbers(a,b,c):
    if a>b:
        if a>c:
            print(a , "is largets number")
        else:
            print(c , "is largets number")
    else:
        if b>c:
            print(b , "is largets number")
        else:
            print(c , "is largets number")
            
maxin3numbers(2,5,3)