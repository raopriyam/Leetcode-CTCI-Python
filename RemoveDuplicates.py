# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 23:33:44 2021

@author: priya
"""

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        
        