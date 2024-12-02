# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:04:13 2024

@author: priya
"""

def arrangeCoins(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    count = 1
    result = 0
    while n>0:
        n = n - count
        if n < 1:
            return result
        result += 1
        count = count + 1
    

