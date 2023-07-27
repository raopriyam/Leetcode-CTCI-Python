# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:39:17 2023

@author: priya
"""

def finalValueAfterOperations(operations):
    x = 0
    for i in operations:
        if i == "--X" or i == "X--":
            x = x-1
        else:
            x = x+1
    return x 

print(finalValueAfterOperations(["--X","++X","X++"]))