# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 21:35:01 2021

@author: priya
"""

def patternJ():
    for i in range(10):
        for j in range(5):
            if i == 0 or j == 2  or (i == 9 and j==1 ) or (i==8 and j==0):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
        
patternJ()
    