# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:36:44 2021

@author: priya
"""

def patternE(n):
    for i in range(n+n-1):
        for j in range(n):
            if i== 0 or i ==n-1 or i==n+n-2 or j==0:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

patternE(7)