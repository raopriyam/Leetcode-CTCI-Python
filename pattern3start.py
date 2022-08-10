# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:22:39 2022

@author: priya
"""

def pattern1(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()
    for i in range(n+1):
        for j in range(i):
            print("*",end=" ")
        print()
            
        
        
        
        
pattern1(5)
pattern1(10)