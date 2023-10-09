# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:42:29 2023

@author: priya
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        setCheck = set()
        left = 0
        count = 0
        for right in range(len(s)):
            while s[right] in setCheck:
                setCheck.remove(s[left])
                left += 1
            setCheck.add(s[right])
            count = max(count,right-left+1)
        return count