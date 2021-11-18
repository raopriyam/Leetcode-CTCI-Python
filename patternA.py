# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:42:52 2021

@author: priya
"""

def patternA(n):
    for i in range(n+n-1):
        for j in range(n):
            if (j== 0 or j==n-1) and i!=0 or ((i == 0 or i == n-1) and (j>0 and j<n-1)):
                print("*",end=" ")
            else:
                print(end = "  ")
        print()
        
patternA(10)