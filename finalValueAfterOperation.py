# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:15:10 2022

@author: priya
"""

def finalValueAfterOperations(arr):
    x = 0
    for i in arr:
        if i == "X--" or i == "--X":
            x = x-1
        elif i == "X++" or i == "++X":
            x = x+1
            
    return x

print(finalValueAfterOperations(["--X","X++","X++"]))

print(finalValueAfterOperations(["++X","++X","X++"]))

print(finalValueAfterOperations( ["X++","++X","--X","X--"]))