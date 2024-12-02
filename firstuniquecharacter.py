# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:35:45 2024

@author: priya
"""

def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    list1 = [0]*26
    if ((len(s) > len(set(s))) and (len(set(s)))) == 1:
        return -1
    else:
        for i in range(len(s)):
            list1[ord(s[i]) - ord("a")] += 1
        for i in range(len(s)):
            if list1[ord(s[i]) - ord("a")] == 1:
                return i


        return -1