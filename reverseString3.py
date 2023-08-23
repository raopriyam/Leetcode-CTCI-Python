# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:46:46 2023

@author: priya
"""

def reverseString( s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    first = 0
    last = len(s)-1
    while first<last:
        temp = s[first]
        s[first] = s[last]
        s[last] = temp
        first = first + 1
        last  = last - 1
    return s

print(reverseString(["p","r","i","y","a","m"]))