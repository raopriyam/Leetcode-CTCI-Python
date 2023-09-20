# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:26:48 2023

@author: priya
"""

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        check = ord(s[0])
        ans = ""
        for i in s:
            if i.isalpha():
                ans = ans + i
                check = ord(i)
            elif i.isdigit():
                ans = ans + chr(check + int(i))
        return ans
        