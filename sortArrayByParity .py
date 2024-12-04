# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:45:50 2024

@author: priya
"""

def sortArrayByParity(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = 0
    ans = []
    while n < len(nums):
        if nums[n] % 2 == 0:
            ans.insert(0,nums[n])
        else:
            ans.append(nums[n])
        n = n+1
    return ans