# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 20:45:08 2026

@author: priya
"""

def repeatedCharacter(self, s: str) -> str:
    set1 = set()
    for i in s:
        if i not in set1:
            set1.add(i)
        else:
            return i

