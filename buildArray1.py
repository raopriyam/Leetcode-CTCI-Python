# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:45:33 2023

@author: priya
"""

def buildArray(nums):
    ans = []
    for i in nums:
        ans.extend([nums[i]])
    return ans

print(buildArray([1,2,4,3,0,5]))