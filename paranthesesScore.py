# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:55:03 2023

@author: priya
"""

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        cur = 0
        for c in s:
            if c == '(':
                stack.append(cur)
                cur = 0
            else:
                cur = stack.pop() + max(1, cur*2)
        return cur 