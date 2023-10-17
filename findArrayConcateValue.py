# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 18:16:54 2023

@author: priya
"""
class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        temp = 0
        while left<right:
            temp = temp + int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        if left == right:
            temp = temp + nums[left]
        return temp
