# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:40:07 2023

@author: priya
"""

def findMissingNumber(list1, n):
    return int(n*(n+1)/2) - sum(list1)

print(findMissingNumber([1,2,3,5,6,7,9,8,10], 10))