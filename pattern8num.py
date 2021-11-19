# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:26:05 2021

@author: priya
"""

def pattern8(n):
    for i in range(n+n-1):
        for j in range(n):
            if i==0 and (j != 0 or j!= n-1) or i==n-1  or i == n+n-2 and (j != 0 or j!= n-1) or j== 0 or j== n-1:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
                
pattern8(5)