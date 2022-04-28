# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:30:21 2022

@author: priya
"""

def buildArray( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for i in nums:
        ans.append(nums[i])
        
    return ans

print(buildArray([0,2,1,5,3,4]))