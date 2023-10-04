# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:46:57 2023

@author: priya
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1 and abs(i - dict1[nums[i]]) <=k:
                return True
            dict1[nums[i]] = i
        return False
    
ob1 = Solution()
output = ob1.containsDuplicate([1,2,3,1],3)

assert output == True
print(output)