# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:44:21 2024

@author: priya
"""

def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    set1 = set(nums)
    ans = []
    for i in range(1, len(nums)+1):
        if i not in set1:
            ans.append(i)
    return ans