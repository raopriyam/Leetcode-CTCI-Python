# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:14:52 2021

@author: priya
"""

def alternatePosNeg(arr):
    pos =0
    neg = 1
    ans = []
    for i in arr:
        if i>0:
            ans.insert(pos,i)
            pos += 2
        elif i<0:
            ans.insert(neg,i)
            neg += 2
    return ans


print(alternatePosNeg([9, 4, -2, -1, 5, 0, -5, -3, 2]))