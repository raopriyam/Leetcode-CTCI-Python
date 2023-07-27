# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:56:52 2023

@author: priya
"""

def getConcatenation(nums):
    nums.extend(nums)
    return nums

print(getConcatenation([1,2,1]))