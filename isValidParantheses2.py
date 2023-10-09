# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:29:29 2023

@author: priya
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        Dictionary = {")":"(",
                        "}": "{",
                        "]":"["}
        for i in s:
            if i in Dictionary:
                if stack and stack[-1] == Dictionary[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True