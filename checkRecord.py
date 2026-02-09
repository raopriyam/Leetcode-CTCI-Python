# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 20:05:25 2026

@author: priya
"""

def checkRecord(self, s: str) -> bool:
    A = 0
    L = 0

    for i in s:
        if i == 'A':
            A += 1
            L = 0
        elif i == 'L':
            L += 1
            if L >= 3:
                return False
