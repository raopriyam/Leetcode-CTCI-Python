# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 22:32:23 2023

@author: priya
"""

def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict1 = {}
    ans = []
    for i in range(len(nums)):
        if (target - nums[i]) not in dict1:
            dict1[nums[i]] = i
        else:
            ans.append(dict1[(target - nums[i])])
            ans.append(i)
    return ans

print(twoSum([2,7,11,15], 9))