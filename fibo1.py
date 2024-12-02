# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:49:44 2024

@author: priya
"""

def fib(self, n):
    """
    :type n: int
    :rtype: int
    """
    first = 0
    second = 1
    if n == 0:
        return first
    elif n == 1:
        return second
    elif n > 1:
        count = 1
        while count<n:
            count += 1
            nextnum = first + second
            first = second
            second = nextnum
        return nextnum