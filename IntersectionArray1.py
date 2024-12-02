# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:40:23 2024

@author: priya
"""

def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    set1, set2 = set(nums1), set(nums2)
    ans = []
    for i in set1:
        if i in set2:
            ans.append(i)
    return ans