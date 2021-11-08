# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:14:20 2021

@author: priya
"""

def removeVowels(s):
    s = list(s)
    i = 0
    n = len(s)-1
    set1 = {"a","A","e","E","i","I","o","O","u","U"}
    while i<=n:
        if s[i] in set1:
            s.remove(s[i])
        else:
            i +=1
        n = len(s)-1
    
    return "".join(s)

print(removeVowels("priyam"))