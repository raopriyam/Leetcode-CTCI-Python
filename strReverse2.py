# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 23:30:50 2021

@author: priya
"""

def strReverse2(s):
    ans = []
    #print(s.split(" "))
    for i in s.split(" "):
        ans.append(i[::-1])
    return (ans)
print(strReverse2("my name is priyam rao"))
        
        