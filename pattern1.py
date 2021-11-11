# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 23:15:37 2021

@author: priya
"""

def pattern(n):
    for i in range(n+1):
        for j in range(i):
            print("*",end ="")
        print()

pattern(5)
            