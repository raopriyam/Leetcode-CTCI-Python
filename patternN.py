# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 23:36:04 2021

@author: priya
"""

def patternN(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j==n-1 or i==j:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

patternN(7)    
    