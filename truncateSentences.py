# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:41:47 2023

@author: priya
"""

def truncateSentence(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    ans = ""
    check = 0
    i = 0
    while check < k and i < len(s):
        if s[i] == " ":
            check = check + 1
        ans = ans + s[i]
        i += 1
    return ans

print(truncateSentence(s = "Hello how are you Contestant", k = 4))