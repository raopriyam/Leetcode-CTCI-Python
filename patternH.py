# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:40:14 2021

@author: priya
"""

def patternH(n):
    for i in range(n+n-1):
        for j in range(n):
            if j== 0 or i ==n-1 or j==n-1:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
        
patternH(7)