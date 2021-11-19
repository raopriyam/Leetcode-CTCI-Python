# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:40:40 2021

@author: priya
"""

def pattern3num(n):
    for i in range(n+n-1):
        for j in range(n):
            if i == 0 or i == n-1 or i == n+n-2 or j == n-1:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
        
pattern3num(5)
                