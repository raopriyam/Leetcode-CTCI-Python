# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 03:06:06 2025

@author: priya
"""

def summaryRanges( nums):
    if not nums:
        return []

    res = []
    start = nums[0]

    for i in range(1, len(nums)):
        # if next number is not consecutive, close the current range
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i - 1]}")
            start = nums[i]

    # finalize the last range
    if start == nums[-1]:
        res.append(str(start))
    else:
        res.append(f"{start}->{nums[-1]}")

    return res
