# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:10:23 2023

@author: priya
"""

def leftRightDifference( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    leftSum = []
    rightSum = []
    ans = []
    leng = len(nums)
    check = 0
    for i in range(leng):
        leftSum.append(sum(nums[:check]))
        rightSum.append(sum(nums[check+1:]))
        check += 1
    for i in range(leng):
        ans.append(abs(leftSum[i]-rightSum[i]))
    return ans

print(leftRightDifference([10,4,8,3]))