# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:54:13 2023

@author: priya
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
                i -= 1
            i += 1
        return nums