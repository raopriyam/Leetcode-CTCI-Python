# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:37:03 2023

@author: priya
"""

def numIdenticalPairs(nums):
    check = 0
    for i in range(len(nums)):
        for j in nums[i+1:]:
            if nums[i] == j:
                check += 1

    return check

print(numIdenticalPairs([1,2,3,1,1,3]))