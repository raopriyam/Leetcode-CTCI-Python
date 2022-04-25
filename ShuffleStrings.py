# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:16:36 2022

@author: priya
"""

def shuffleStrings(s,indices):
    final = []
    for i in indices:
        final.insert(i,s[i])
    return " ".join(final)

print(shuffleStrings("codeleet", [4,5,6,7,0,2,1,3]))
        