# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 23:43:34 2025

@author: priya
"""

def revString2(s):
    ans = ""
    for i in range(len(s)-1,-1,-1):
        ans = ans + s[i]
    return ans

print(revString2("Priyam"))