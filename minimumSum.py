# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:05:01 2022

@author: priya
"""

def minimumSum(num):
    """
    :type num: int
    :rtype: int
    """
    nums = list(str(num))
    nums.sort()
    ans1 = nums[0]+nums[2]
    ans2 = nums[1]+nums[3]
    return int(ans1)+int(ans2)

print(minimumSum(2932))