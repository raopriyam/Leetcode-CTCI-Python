# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 02:03:54 2025

@author: priya
"""

def findMaxConsecutiveOnes( nums):
    finalCount = 0
    check = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            check += 1
        else:
            check = 0
        if check > finalCount:
            finalCount = check

    return finalCount


print(findMaxConsecutiveOnes([1,1,0,1,1,1]))