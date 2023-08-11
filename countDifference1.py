# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:52:48 2023

@author: priya
"""

def countKDifference( nums, k):
 """
 :type nums: List[int]
 :type k: int
 :rtype: int
 """
 check = 0
 for i in range(len(nums)):
     for j in nums[i+1:]:
         if abs(nums[i] - j) == k:
             check += 1
 return check

print(countKDifference([1,2,2,1], 1))