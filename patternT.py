# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:46:39 2021

@author: priya
"""

def patternT(n):
    for i in range(n+n-1):
        for j in range(n):
            if i==0 or j == n//2:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

patternT(5)