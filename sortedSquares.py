# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:46:18 2024

@author: priya
"""
def sortedSquares(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(len(nums)):
        nums[i] = nums[i]*nums[i]
    
    nums.sort()
    return nums
