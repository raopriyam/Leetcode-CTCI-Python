# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:11:55 2023

@author: priya
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        leng = len(needle)
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if i+leng <= len(haystack) and (haystack[i:i+leng] == needle or haystack[i] == needle):
                return i
        return -1