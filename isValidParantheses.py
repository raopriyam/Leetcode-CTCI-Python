# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:50:59 2023

@author: priya
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = [0,0,0]
        if s == "" or s == " ":
            return False

        for i in s:
            if i == "(":
                ans[0] += 1
            elif i == ")":
                ans[0] -= 1
            elif i == "{":
                ans[1] += 1
            elif i == "}":
                ans[1] -= 1
            elif i == "[":
                ans[2] += 1
            else:
                ans[2] -= 1
            if -1 in ans:
                return False
        return ans == [0,0,0]