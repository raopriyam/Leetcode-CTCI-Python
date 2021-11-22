# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:49:33 2021

@author: priya
"""

def pattern06(n):
    for i in range(n+n-1):
        for j in range(n):
            if i == 0 or i==n-1 or i==n+n-2 or j == 0 or j==n-1 and i>=n:
                print("*",end = " ")
            else:
                print(end = "  ")
        print()
        
pattern06(4)