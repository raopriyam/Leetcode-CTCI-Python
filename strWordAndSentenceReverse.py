# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 23:45:37 2021

@author: priya
"""

def strWordAndSentenceReverse(s):
    ans = []
    s = s.split(" ")
    #print(s.split(" "))
    for i in s:
        ans.append(i[::-1])
    left = 0
    right = len(s)-1
    while left<right:
        temp = ans[left]
        ans[left] = ans[right]
        ans[right] = temp
        left += 1
        right -= 1
    return " ".join(ans)

print(strWordAndSentenceReverse("my name is priyam rao1"))
    
    