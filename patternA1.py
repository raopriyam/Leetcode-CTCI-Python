# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 23:08:40 2021

@author: priya
"""

def patternA(n):
    for i in range(n+n-1):
        for j in range(n):
            if ((i == 0 or i==n//2+1) and (j >=1 and j<n-1)) or ((j==0 or j==n-1) and (i >0 and i<n+n-2)):
                print("*",end=" ")
            else:
                print(end= "  ")
        print()
        
        
patternA(5)