# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:00:44 2023

@author: priya
"""

class Solution(object):
    def anagramMappings(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        ans = []
        for i in range(len(nums2)):
            dict1[nums2[i]] = i
        for i in nums1:
            ans.append(dict1[i])
        return ans 