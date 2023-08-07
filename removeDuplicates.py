# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 23:17:29 2023

@author: priya
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = list(set(nums))
    print(nums)
    return len(nums)

print(removeDuplicates([1,1,2]))