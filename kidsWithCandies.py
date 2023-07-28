# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:37:50 2023

@author: priya
"""

def kidsWithCandies(candies, extraCandies):
    ans = []
    maxCandies = max(candies)
    for i in candies:
        if i+extraCandies >= maxCandies:
            ans.append(True)
        else:
            ans.append(False)
    return ans

print(kidsWithCandies([2,3,5,1,3], 3))