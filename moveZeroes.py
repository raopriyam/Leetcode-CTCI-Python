# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 18:25:40 2023

@author: priya
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        leng = len(nums) - 1
        i = 0
        while i<= leng:
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
            i+= 1
        return nums