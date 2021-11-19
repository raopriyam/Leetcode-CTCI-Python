# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:33:38 2021

@author: priya
"""

def pattern2(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i == n-1 or j == n-1:
                print("*",end=" ")
            else:
                print(end="  ")
        print()
    for i in range(n,n+n-1):
        for j in range(n):
            if j == 0 or i == n+n-2:
                print("*",end=" ")
            else:
                print(end=" ")
        print()
                
pattern2(5)