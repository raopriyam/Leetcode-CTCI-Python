# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:29:15 2023

@author: priya
"""

class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        setString = set(s)
        if "|" not in setString:
            return 0
        else:
            S_array = s.split("|")
            count = 0
            for i in range(2,len(S_array),2):
                for j in S_array[i]:
                    if j == "*":
                        count += 1
            return count