# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 19:56:37 2025

@author: priya
"""

def isIsomorphic(self, s: str, t: str) -> bool:
    slen= len(s)
    tlen = len(t)
    dict1 = {}
    dict2 = {}
    if slen != tlen:
        return False
    for i in range(slen):
        if s[i] not in dict1:
            dict1[s[i]] = t[i]
        else:
            if dict1[s[i]] != t[i]:
                return False

        if t[i] not in dict2:
            dict2[t[i]] = s[i]
        else:
            if dict2[t[i]] != s[i]:
                return False
    return True
