# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:55:26 2023

@author: priya
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        setCheck = set()
        count = 0
        ans = 0
        i = 0
        while i< len(s):
            if s[i] not in setCheck:
                setCheck.add(s[i])
                count += 1
                i += 1
            else:
                setCheck.clear()
                count = 0
            if count >= ans:
                ans = count
        return ans