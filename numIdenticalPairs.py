# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:46:29 2022

@author: priya
"""

def numIdenticalPairs( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    nums1 = set(nums)
    for i in nums1:
        a = nums.count(i)
        if a>1:
            a = (a*(a-1))/2
            count = count+a
    return int(count)


print(numIdenticalPairs([1,2,3,1,1,3]))