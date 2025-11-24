# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 20:06:27 2025

@author: priya
"""

def wordPattern(self, pattern: str, s: str) -> bool:
    list1 = s.split(" ")
    dict1 = {}
    dict2 = {}
    if len(pattern) != len(list1):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in dict1:
            dict1[pattern[i]] = list1[i]
        else:
            if dict1[pattern[i]] != list1[i]:
                return False
            
        if list1[i] not in dict2:
            dict2[list1[i]] = pattern[i]
        else:
            if dict2[list1[i]] != pattern[i]:
                return False

    return True
