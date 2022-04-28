# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:12:26 2022

@author: priya
"""

def removeElement( nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count= 0
    ln = len(nums)
    while count<ln:
        if nums[count]==val:
            nums.remove(nums[count])
            ln = ln-1
        else:
            count = count+1
    return nums, ln

print(removeElement([1,2,3,4,2,3,5,6,2,7,8,4,2,6,4,9,0],2))