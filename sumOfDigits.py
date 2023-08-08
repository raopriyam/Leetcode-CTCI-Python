# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:30:14 2023

@author: priya
"""

def sumOfDigits(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    minNum = min(nums)
    check = [int(i) for i in str(minNum)]
    if sum(check)%2 == 0:
        return 1
    else:
        return 0
    
print(sumOfDigits([34,23,1,24,75,33,54,8]))