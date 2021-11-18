# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:34:55 2021

@author: priya
"""

def pattern9(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
        
pattern9(5)
        