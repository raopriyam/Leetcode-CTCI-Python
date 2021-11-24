# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:33:14 2021

@author: priya
"""

def patternD(n):
    for i in range(n+n-1):
        for j in range(n):
            if j == 1 or (i == 0 and j!=n-1) or (i == n+n-2 and j!= n-1) or j == n-1:
                print("*",end=" ")
            else:
                print(end="  ")
                
        print()
        
        
patternD(7)