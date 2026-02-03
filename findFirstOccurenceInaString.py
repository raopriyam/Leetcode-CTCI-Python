# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 14:15:48 2026

@author: priya
"""

def strStr(self, haystack: str, needle: str) -> int:
    start = 0
    end = len(needle)-1
    while end < len(haystack):
        if haystack[start:end+1] == needle:
            return start
        else:
            start += 1
            end += 1
    return -1