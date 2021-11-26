# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 23:16:42 2021

@author: priya
"""

def patternB(n):
    for i in range(n+n-1):
        for j in range(n):
            if j == 0 or (i==0 and (j>0 and j<n-1))or (i==n-1 and (j>0 and j<n-1)) or (i==n+n-2 and (j>0 and j<n-1) ) or (j==n-1 and (i!=0 and i!=n-1 and i!=n+n-2)):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
        
patternB(5)
    