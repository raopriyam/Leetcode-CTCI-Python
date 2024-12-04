# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:44:59 2024

@author: priya
"""

def isMonotonic(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    check = nums[:]
    check.sort()
    if check == nums or check[::-1] == nums:
        return True
    return False