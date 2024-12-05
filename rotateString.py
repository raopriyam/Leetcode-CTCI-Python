# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:32:52 2024

@author: priya
"""

def rotateString(self, s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    if s == goal:
        return True
    elif len(s) != len(goal):
        return False
    else:
        for i in range(len(s)):
            if s == (goal[i:] + goal[:i]):
                return True
    return False