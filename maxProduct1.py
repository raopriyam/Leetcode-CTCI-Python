# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 23:26:52 2023

@author: priya
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum1 = max(nums)
        nums.remove(maxNum1)
        maxNum2 = max(nums)
        return (maxNum1-1)*(maxNum2-1)