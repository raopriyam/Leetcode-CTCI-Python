# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:38:07 2023

@author: priya
"""

def removeVowels(s):
    """
    :type s: str
    :rtype: str
    """
    ans = ""
    set1 = {"a","e","i","o","u"}
    for i in s:
        if i not in set1:
            ans = ans + i
    return ans

print(removeVowels("mynameisPriyamRao"))