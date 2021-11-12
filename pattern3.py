# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 23:26:46 2021

@author: priya
"""

def pattern3(n):
    for i in range(n+1):
        for j in range(i):
            print(j,end=" ")
        print()
            
pattern3(5)