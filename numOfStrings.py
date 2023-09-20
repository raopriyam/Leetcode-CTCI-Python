# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:38:43 2023

@author: priya
"""

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0
        for i in patterns:
            if i in word:
                count += 1
        return count