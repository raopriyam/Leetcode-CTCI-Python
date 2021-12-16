# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 23:40:59 2021

@author: priya
"""

def ListCheck(ls1):
    for i in ls1:
        if i == 0:
            return False
    return True 

print(ListCheck([1,2,3,4,5]))
    