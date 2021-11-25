# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:39:51 2021

@author: priya
"""

def patternJ(n):
    for i in range(n+n-1):
        for j in range(n):
            if i ==0 or ((j == n//2) and (i<n+n-2)) or ((i == n+n-2) and (j<n//2)):
                print("*",end=" ")
            else:
                print(end = "  ")
        print()
        
patternJ(5)