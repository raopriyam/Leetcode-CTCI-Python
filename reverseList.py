# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:38:41 2021

@author: priya
"""

def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s)-1
    while left<right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
    return s

print(reverseString(["p","r","i","y","a","m"]))