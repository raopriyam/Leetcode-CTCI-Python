# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:56:52 2023

@author: priya
"""

def getConcatenation(nums):
    leng = len(nums)
    for i in range(leng):
        nums.append(nums[i])
    return nums

print(getConcatenation([1,2,1]))