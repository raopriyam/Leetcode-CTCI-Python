# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 08:41:02 2026

@author: priya
"""

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    l = 0
    r = len(s)-1
    while l<r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp

        l += 1
        r -= 1
    