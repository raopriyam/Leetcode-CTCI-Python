# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 13:38:32 2026

@author: priya
"""


def findMin( nums):
    l = 0
    r = len(nums)-1
    while l < r:
        m = (l+r) // 2
        if nums[m] > nums[r]:
            l = m+1
        else:
            r = m
    return nums[l]
    