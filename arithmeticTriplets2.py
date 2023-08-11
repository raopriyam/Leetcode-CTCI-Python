# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:38:17 2023

@author: priya
"""

def arithmeticTriplets(nums, diff):
    """
    :type nums: List[int]
    :type diff: int
    :rtype: int
    """
    set1 = set(nums)
    check = 0
    for i in nums:
        if (i+diff in set1) and (i+(2*diff) in set1):
            check += 1
    return check

print(arithmeticTriplets([0,1,4,6,7,10], 3))