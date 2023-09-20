# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:02:19 2023

@author: priya
"""

class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        ans = ""
        for i in range(len(words)):
            ans = ans + words[i]
            if s in ans:
                break
        if s == ans:
            return True
        return False