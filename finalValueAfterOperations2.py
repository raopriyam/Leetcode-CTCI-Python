# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:43:29 2023

@author: priya
"""

def finalValueAfterOperations(operations):
    a=operations.count("++X")+operations.count("X++")
    return (2*a-len(operations))


print(finalValueAfterOperations(["--X","++X","X++"]))