# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 13:32:19 2026

@author: priya
"""


def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1]*n

    product1 = 1
    for i in range(n):
        result[i] = product1
        product1 = product1*nums[i]
    
    product2 = 1
    for i in range(n-1,-1,-1):
        result[i] = product2*result[i]
        product2 = product2*nums[i]

    return result
    