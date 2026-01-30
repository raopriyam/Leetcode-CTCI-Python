# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 16:42:22 2026

@author: priya
"""

def validPalindrome(self, s: str) -> bool:
    if not s:
        return False
    for i in range(len(s)):
        ans = s[:i] + s[i+1:]
        if ans == ans[::-1]:
            return True
    return False