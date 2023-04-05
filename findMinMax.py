# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:50:27 2023

@author: priya
"""

import math

def findMinMax(list1):
    min1 = math.inf
    max1 = -math.inf
    for i in list1:
        if i<=min1:
            min1 = i
        if i>=max1:
            max1 = i
    return "min is ",min1," max is ",max1

print(findMinMax([2,3,1,4,5,6,7,99,8,0]))