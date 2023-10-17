# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 18:58:23 2023

@author: priya
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        i = 0
        while i<len(nums) :
            if nums[i] == val:
                nums.remove(val)
                i -= 1
            i+=1
        return count,nums
    
