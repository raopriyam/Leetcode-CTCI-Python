# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:36:10 2023

@author: priya
"""

def arithmeticTriplets( nums, diff):
    """
    :type nums: List[int]
    :type diff: int
    :rtype: int
    """
    check = 0
    for i in nums:
        if (i+diff in nums) and (i+(2*diff) in nums):
            check += 1
    return check

print(arithmeticTriplets([0,1,4,6,7,10], 3))