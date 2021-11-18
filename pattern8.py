# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:57:56 2021

@author: priya
"""

def pattern8(n):
    for i in range(n):
        for j in range(n-i-1):
            print(end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
    
pattern8(5)