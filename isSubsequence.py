# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 20:01:17 2026

@author: priya
"""

def isSubsequence(self, s: str, t: str) -> bool:
    len_s = len(s)
    len_t = len(t)
    ns = 0
    nt = 0
    
    while nt < len_t and ns < len_s:
        if s[ns] == t[nt]:
            ns += 1
            nt += 1

        else:
            nt += 1

    if ns == len_s :
        return True
    return False
