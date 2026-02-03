# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:52:22 2026

@author: priya
"""

def reverseDegree(self, s: str) -> int:
    total = 0
    for i in range(len(s)):
        pos = ord(s[i]) - ord('a')
        reverse = 26 - pos
        total = total + (i+1)*reverse

    return total
