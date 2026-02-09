# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 20:30:00 2026

@author: priya
"""

def minimumMoves(self, s: str) -> int:
    n = 0
    counter = 0
    while n < len(s):
        if s[n] == 'X':
            n = n + 3
            counter += 1 
        else:
            n += 1
    return counter