# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 19:10:48 2025

@author: priya
"""

def isIsomorphic( s, t):
    slen= len(s)
    tlen = len(t)
    dict1 = {}
    if slen != tlen:
        return False
    for i in range(slen):
        if s[i] not in dict1:
            dict1[s[i]] = t[i]
        else:
            if dict1[s[i]] != t[i]:
                return False
    return True