# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:27:25 2023

@author: priya
"""

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        leng = len(nums)
        while i<len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
            i += 1
        for i in range(leng):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
        return nums