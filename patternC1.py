# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 23:24:42 2021

@author: priya
"""

def patternC():
    for i in range(7):
        for j in range(5):
            if ((i == 0 or i==6 ) and (j>0 and j<4)) or (j == 0 and (i>0 and i<6)) or (j==4 and (i == 1 or i==5)):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
    
patternC()