# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:02:17 2023

@author: priya
"""

def productArray(nums):
    left = [1]*len(nums)
    right = [1]*len(nums)
    n = len(nums)
    ans = []
    
    for i in range(1,len(nums)-1):
        left[i-1] = left[i]*nums[i]
        
    for i in range(len(nums)-1):
        left[n-i-1] = left[n-i]*nums[n-i]
    
    for i in range(n):
        ans[i] = left[i]*right[i]
    
    return ans

print(productArray(nums = [1,2,3,4]))