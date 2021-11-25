# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:44:13 2021

@author: priya
"""

def patternL(n):
    for i in range(n+n-1):
        for j in range(n):
            if j==0 or i == n+n-2:
                print("*",end=" ")
            else:
                print(end = "  ")
        print()
        
        
patternL(5)