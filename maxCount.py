# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:31:41 2021

@author: priya
"""

def maxCount(nums):
    arr = nums
    nums = list(set(nums))
    count = 0
    for i in nums:
        count = max(count,arr.count(i))
        
    return count


print(maxCount([1,2,2,3,1]))