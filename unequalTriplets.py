# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:39:42 2023

@author: priya
"""

def unequalTriplets(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    check = len(set(nums))
    if check<3:
        return 0
    elif len(nums) == 3:
        return 1
    else:
        return check
    
print(unequalTriplets([4,4,2,4,3]))