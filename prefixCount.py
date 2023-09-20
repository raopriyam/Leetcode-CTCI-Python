# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:40:29 2023

@author: priya
"""

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        leng = len(pref)
        for i in words:
            if i[0:leng] == pref:
                count += 1
        return count