# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:34:52 2021

@author: priya
"""

def squareOfSortedArray(nums):
    i = 0
    while i<len(nums):
        nums[i] = nums[i]*nums[i]
        i += 1
    nums.sort()
    return nums

print(squareOfSortedArray([-4,-1,0,3,10]))