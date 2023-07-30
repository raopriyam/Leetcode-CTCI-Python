# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:47:59 2023

@author: priya
"""

def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans1 = {}
    ans = []

    leng = len(nums)
    for i in range(leng):
        ans1[nums[i]] = i
    nums.sort()
    check = 0

    for i in range(leng):
        if i > 0 and nums[i] == nums[i-1]:
            ans1[nums[i]] = check
        else:
            ans1[nums[i]] = check
            check = check+1
    for i in ans1:
        ans.append(ans1[i])
    return ans

print(smallerNumbersThanCurrent([8,1,2,2,3]))