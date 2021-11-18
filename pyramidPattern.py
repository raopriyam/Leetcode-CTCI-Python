# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:38:36 2021

@author: priya
"""

def pattern10(n):
    for i in range(n):
        for j in range(n-i-1):
            print(end=" ")
        for i in range(i+1):
            print("*",end=" ")
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
pattern10(5)
        