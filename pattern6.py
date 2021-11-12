# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 23:36:55 2021

@author: priya
"""

def pattern6(n):
    for i in range(n):
        for j in range(n-i,0,-1):
            print("*",end=" ")
        print()
        
pattern6(10)