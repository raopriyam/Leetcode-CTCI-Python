# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:22:27 2026

@author: priya
"""

def isAnagram(self, s: str, t: str) -> bool:
    if set(s) == set(t) and len(s) == len(t):
        return True
    else:
        return False