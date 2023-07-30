# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:31:18 2023

@author: priya
"""

def smallerNumbersThanCurrent( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for i in nums:
        check = 0
        for j in nums:
            if i>j:
                check += 1
        ans.append(check)
    return ans

print(smallerNumbersThanCurrent( [10,2,8,4,5]))