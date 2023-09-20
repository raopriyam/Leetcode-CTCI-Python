# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:26:09 2023

@author: priya
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = [0]*26
        for i in s:
            temp = ord(i)    
            ans[temp-97] += 1
        return len(list(set(ans))) <= 2