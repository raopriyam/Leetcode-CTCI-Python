# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:23:15 2023

@author: priya
"""

def runningSum2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sum1 = 0
    leng = len(nums)
    for i in range(leng):
        sum1 = sum1 + nums[i]
        nums.append(sum1)
    return nums[leng:]


print(runningSum2([1,2,3,4,5]))