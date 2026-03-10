# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:46:42 2026

@author: priya
"""


def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    set1 = set(nums)
    maxCount = 0
    for i in set1:
        currCount = nums.count(i)
        if currCount > maxCount:
            MElement = i
            maxCount = currCount
    if maxCount > len(nums)//2 :
        return MElement
