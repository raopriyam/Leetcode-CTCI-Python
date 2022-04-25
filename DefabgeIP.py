# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:02:47 2022

@author: priya
"""

def defangIP(s):
    final = ""
    for i in range(len(s)):
        if s[i] == ".":
            final = final + "[" + s[i] + "]"
        else:
            final = final + s[i]
    return final 

print(defangIP("1.1.1.1"))