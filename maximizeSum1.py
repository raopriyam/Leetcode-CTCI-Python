# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 23:22:38 2023

@author: priya
"""

class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tempMax = max(nums)
        count = k
        total = 0
        while count>0:
            total = total + tempMax
            tempMax += 1
            count -= 1
        return total