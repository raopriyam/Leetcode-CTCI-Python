# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 16:03:49 2026

@author: priya
"""

def rotateString(self, s: str, goal: str) -> bool:
    for i in range(len(s)):
        ans = s[i:] + s[:i]
        if ans == goal:
            return True
    return False
    