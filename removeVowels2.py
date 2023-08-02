# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:05:02 2023

@author: priya
"""

def removeVowels(s):
    """
    :type s: str
    :rtype: str
    """
    set1 = {"a","e","i","o","u"}
    leng = len(s)
    for i in range(leng):
        if s[i] not in set1:
            s = s + s[i]
    return s[leng:]


print(removeVowels("mynameisPriyamRao"))