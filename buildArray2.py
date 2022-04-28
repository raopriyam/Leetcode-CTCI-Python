# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:41:14 2022

@author: priya
"""

def buildArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [0]*len(nums)
    for i in range(len(nums)):
        #ans.append(nums[i])
        ans[i] = nums[nums[i]]
        
    return ans

print(buildArray([[5,0,1,2,3,4]]))