# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:19:03 2022

@author: priya
"""

def lengthOfLastWord( s):
    """
    :type s: str
    :rtype: int
    """
    ans = s.split(" ")
    for i in ans[::-1]:
        if (i.isalpha()):
            return len(i)   
    return ""


print(lengthOfLastWord("my name is priyam rao"))