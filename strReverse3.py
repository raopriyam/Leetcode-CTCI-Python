# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 23:38:11 2021

@author: priya
"""

def strReverse3(s):
    s = s.split(" ")
    left = 0
    right = len(s)-1
    while left<right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
    return " ".join(s)

print(strReverse3("my name is priyam rao"))
        