# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:30:51 2021

@author: priya
"""

def patternC(n):
    for i in range(n+n-1):
        for j in range(n):
            if j == 0 or i == 0 or i == n+n-2:
                print("*",end=" ")
            else:
                print(end = "  ")
        print()
                
patternC(5)