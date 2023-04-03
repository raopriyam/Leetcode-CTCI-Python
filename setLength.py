# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:18:53 2023

@author: priya
"""

def setLength(set1):
    count = 0
    for i in set1:
        count += 1
    return count,set1


print(setLength({1,2,4,3,5,6,7,8,9,10}))
        