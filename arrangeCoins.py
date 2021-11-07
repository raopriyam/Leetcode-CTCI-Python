# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:34:09 2021

@author: priya
"""

def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    i = 0
    while i<n:
        i += 1
        n = n-i
        
    return i

print(arrangeCoins(5))
        