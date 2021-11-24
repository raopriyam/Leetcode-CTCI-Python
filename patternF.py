# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:39:02 2021

@author: priya
"""

def patternF(n):
      for i in range(n+n-1):
        for j in range(n):
            if i== 0 or i ==n-1 or j==0:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

patternF(7)