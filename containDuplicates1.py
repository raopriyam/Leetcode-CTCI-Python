# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:21:32 2023

@author: priya
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        

ob1 = Solution()
output = ob1.containsDuplicate([1,2,3,1])

assert output == True
print(output)
