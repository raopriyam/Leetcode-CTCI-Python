# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:34:18 2023

@author: priya
"""

def createTargetArray( nums, index):
    """
    :type nums: List[int]
    :type index: List[int]
    :rtype: List[int]
    """
    leng = len(nums)
    ans = [0]*leng
    for i in range(leng):
        ans[index[i]] = nums[i]
        print(ans)
    return ans

print(createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))