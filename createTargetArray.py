# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:43:45 2023

@author: priya
"""

def createTargetArray( nums, index):
    """
    :type nums: List[int]
    :type index: List[int]
    :rtype: List[int]
    """
    leng = len(nums)
    ans = []
    for i in range(leng):
        ans.insert(index[i],nums[i])
    return ans

print(createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))