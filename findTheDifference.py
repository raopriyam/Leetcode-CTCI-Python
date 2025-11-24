# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 23:19:42 2025

@author: priya
"""

def findTheDifference(self, s: str, t: str) -> str:
    freq_s = [0]*26
    freq_t = [0]*26

    for i in s:
        freq_s[ord(i) - ord('a')] += 1

    for i in t:
        freq_t[ord(i)-ord('a')] += 1

    for i in range(26):
        if freq_s[i] != freq_t[i]:
            return chr(i+ord('a'))
    