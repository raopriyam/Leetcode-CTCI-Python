# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 23:33:48 2021

@author: priya
"""

def pattern5(n):
    for i in range(n):
        for j in range(n):
            if (i+j) %2 == 0:
                print("w",end=" ")
            else:
                print("b",end = " ")
        print()
            
pattern5(8)