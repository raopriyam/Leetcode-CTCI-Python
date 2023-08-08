# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 21:45:43 2023

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
    for i in nums:
        if i>9:
            while i>0:
                n = i%10
                sum2 = sum2 + n
                i = i/10
        else:
            sum2 = sum2 + i
    return abs(sum1-sum2)

print(differenceOfSum([1,15,6,3]))