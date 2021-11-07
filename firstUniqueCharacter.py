# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:47:12 2021

@author: priya
"""

def firstUniqChar(s):
    count = 0
    for i in s:
        if s.count(i) == 1:
            return count
        count += 1
    return -1