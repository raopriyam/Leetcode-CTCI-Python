# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:56:28 2023

@author: priya
"""

class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        wordString = "".join(words)
        return s == wordString[0:len(s)]