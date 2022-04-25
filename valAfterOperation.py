# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:54:32 2022

@author: priya
"""

def valAfterOperation(n):
    ans = []
    ans.append(++n)
    ans.append(--n)
    ans.append(++n)
    return ans
print(valAfterOperation(5))