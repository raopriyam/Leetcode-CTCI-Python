# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:39:33 2021

@author: priya
"""

def pattern04(n):
    for i in range(n+n-1):
        for j in range(n):
            if i == n-1 or (j==0 and i<n) or j==n-1:
                print("*",end=" ")
            else:
                print(end = "  ")
        print()
    
pattern04(5)