# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:53:33 2023

@author: priya
"""

def buildArray2(nums):
    leng = len(nums)
    for i in range(leng):
        nums.append(nums[nums[i]])
    return nums[leng::]

print(buildArray2([1,2,3,0,5,4,6,7]))