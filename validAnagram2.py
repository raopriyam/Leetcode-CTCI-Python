# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 15:06:38 2026

@author: priya
"""

def isAnagram(self, s: str, t: str) -> bool:
    s1 = list(s)
    t1 = list(t)

    s1.sort()
    t1.sort()

    print(s1)
    print(t1)