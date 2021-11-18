# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:09:24 2021

@author: priya
"""

def pattern7(n):
    for i in range(n+n-2):
        for j in range(n+1):
            if j == 0 or j == 4 or i == n-1 and (j >= 0 and j<=4):
                print("*", end =" ")
            else:
                print(end="  ")
        print()



pattern7(7)