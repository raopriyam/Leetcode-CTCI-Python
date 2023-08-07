# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 22:53:31 2023

@author: priya
"""

def sumOfMultiples( n):
    """
    :type n: int
    :rtype: int
    """
    sum1 = 0
    for i in range(1,n+1):
        if (i%3 == 0) or (i%5 == 0) or (i%7 == 0):
            sum1 = sum1 + i
    return sum1

print(sumOfMultiples(7))