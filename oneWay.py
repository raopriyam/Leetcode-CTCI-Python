# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 18:09:46 2021

@author: priya
"""

def oneAway(s1,s2):
    ans = 0
    dict1 = {}
    count = 0
    if len(s1) >= len(s2):
        for i in s1:
            dict1[i] = count
            count += 1
        for i in s2:
            if i not in dict1:
                ans += 1
    else:
        for i in s2:
            dict1[i] = count
            count += 1
        for i in s1:
            if i not in dict1:
                ans += 1
        
    return ans

a = oneAway("Priyam","Priy")
print(a)
if a>1:
    print(False)
else:
    print(True)