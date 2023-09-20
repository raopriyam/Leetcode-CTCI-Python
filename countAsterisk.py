# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:29:32 2023

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
            lineCount = 0
            count = 0
            for i in range(len(s)):
                if lineCount % 2 == 0 and lineCount > 0 and s[i] == "*":
                    count += 1
                    print(s[i-2],s[i-1],s[i])
                    print(count)
            
                if s[i] == "|":
                    lineCount += 1
            return count