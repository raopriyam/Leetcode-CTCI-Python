# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:22:04 2023

@author: priya
"""

def runningSum1(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    sum1 = 0
    for i in nums:
        sum1 = sum1 + i
        ans.append(sum1)
    return ans

print(runningSum1([1,2,3,4,5]))