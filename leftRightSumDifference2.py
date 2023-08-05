# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:34:18 2023

@author: priya
"""

def leftRightDifference(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    leftSum = []
    rightSum = []
    ans = []
    leng = len(nums)
    for i in range(leng):
        leftSum.append(sum(nums[:i]))
        rightSum.append(sum(nums[i+1:]))
        ans.append(abs(leftSum[i]-rightSum[i]))
    return ans

print(leftRightDifference([10,4,8,3]))