# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:42:32 2023

@author: priya
"""

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    maxCandies = 0
    for i in candies:
        if i > maxCandies:
            maxCandies = i

    ans = []
    for i in candies:
        if i+extraCandies >= maxCandies:
            ans.append(True)
        else:
            ans.append(False)
    return ans

print(kidsWithCandies([2,3,5,1,3], 3))