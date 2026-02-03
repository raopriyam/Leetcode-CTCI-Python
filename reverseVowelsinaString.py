# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:30:16 2026

@author: priya
"""

def reverseVowels(self, s: str) -> str:
    vowelSet = {'a','e','i','o','u','A','E','I','O','U'}
    l = 0
    r = len(s)-1
    s1 = list(s) 
    while l<r:
        if s1[l] in vowelSet and s1[r] not in vowelSet:
            r -= 1
        elif s1[l] in vowelSet and s1[r] in vowelSet:
            s1[l],s1[r] = s1[r],s1[l]
            l += 1
            r -= 1
        elif s1[l] not in vowelSet and s1[r] in vowelSet:
            l += 1
        else:
            l += 1
            r -= 1

    return "".join(s1)