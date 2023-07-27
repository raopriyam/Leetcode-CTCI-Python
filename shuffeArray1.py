# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:08:07 2023

@author: priya
"""

def shuffleArray( nums, n):
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans

print(shuffleArray([1,2,3,4,5,6], 3))