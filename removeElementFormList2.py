# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:24:18 2021

@author: priya
"""

def removeElementFormList2(nums):
    i = 0
    while i <len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.remove(nums[i+1])
            continue
        i += 1
    return nums
print(removeElementFormList2([0,1,1,2,3,3,4,5,5,5,6]))