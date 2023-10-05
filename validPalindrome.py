# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:00:36 2023

@author: priya
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        else:
            left = 0
            right = len(s)-1
            while left<right:
                if s[left] != s[right]:
                    check1 = s[:left] + s[left+1:]
                    check2 = s[:right] + s[right+1:]
                    return check1 == check1[::-1] or check2 == check2[::-1]
                left += 1
                right -= 1
        return True