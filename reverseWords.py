# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:29:16 2023

@author: priya
"""

def reverseWords( s):
    """
    :type s: str
    :rtype: str
    """
    temp = s.split(" ")
    ans = ""
    for i in temp:
        ans = ans + i[::-1] + " "
    return ans[:len(ans)-1]

print(reverseWords("My name is Priyam Rao"))