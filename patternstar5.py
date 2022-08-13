# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:58:10 2022

@author: priya
"""

def patternstar5(n):
    for i in range(n):
        for j in range(i):
            print("*",end=" ")
        print()
        for j in range(n,n+i):
            print("*",end=" ")
        print()
        

patternstar5(5)
            