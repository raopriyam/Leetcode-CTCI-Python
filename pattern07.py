# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:58:10 2021

@author: priya
"""

def pattern07(n):
    for i in range(1):
        for j in range(n):
            print("*",end=" ")
    for i in range(1,n+n-1):
        for j in range(n-1,0,-1):
            print(" ",end=" ")
        print("*")
        
    
pattern07(5)