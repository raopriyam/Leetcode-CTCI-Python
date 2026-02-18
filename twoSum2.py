# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:29:18 2026

@author: priya
"""
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dictionary = {}
    for i in range(len(nums)):
        if (target - nums[i]) in dictionary:
            return [i,dictionary[target - nums[i]]]
        else:
            dictionary[nums[i]] = i

    



