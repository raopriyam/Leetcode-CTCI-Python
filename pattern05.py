# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:44:06 2021

@author: priya
"""

def pattern05(n):
    for i in range(n+n-1):
        for j in range(n):
            if i == 0 or i == n-1 or i == n+n-2 or j == 0 and i<n or j == n-1 and i>=n and i<n+n-1:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
    
pattern05(5)