# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:40:11 2021

@author: priya
"""

def inList(ls1,target):
    for i in ls1:
        if target == i:
            return True
    return False

print(inList([1,2,3,4,5,6,7,8,9,0],10))