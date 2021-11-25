# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:37:26 2021

@author: priya
"""

def patternI(n):
    for i in range(n+n-1):
        for j in range(n):
            if i == 0 or i==n+n-2 or j==n//2:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
        
        
patternI(5)