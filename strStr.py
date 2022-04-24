# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:35:06 2022

@author: priya
"""

def strStr( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) <1:
        return 0
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and haystack[i:i+len(needle)]==needle:
            return i
    return -1


print(strStr("hello","ll"))
print(strStr("aaaa","bba"))
    