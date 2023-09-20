# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:29:22 2023

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
            if ans[temp - 97] == 0:
                ans[temp-97] = 1
            elif ans[temp - 97] == 1:
                ans[temp-97] = 0
        return ans ==[0]*26