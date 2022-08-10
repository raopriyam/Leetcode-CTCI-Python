# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:17:29 2022

@author: priya
"""

def pattern1(n):
    for i in range(n):
        for j in range(i):
            print("*",end=" ")
        print()
        
        
        
pattern1(5)
pattern1(10)