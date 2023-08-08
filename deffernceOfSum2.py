# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 21:55:10 2023

@author: priya
"""

def differenceOfSum( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum1 = 0
    sum2 = 0
    for i in nums:
        sum1 = sum1 + i
    check = "".join(map(str,nums))
    for i in check:
        sum2 = sum2 + int(i)
    return abs(sum1-sum2)

print(differenceOfSum([1,15,6,3]))