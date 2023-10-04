# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:10:40 2023

@author: priya
"""

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(list(set(nums) - {0})) 
    
ob1 = Solution()
output = ob1.minimumOperations([1,2,3,1])

assert output == 3
print(output)