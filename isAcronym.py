# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:28:03 2023

@author: priya
"""

def isAcronym(words, s):
    """
    :type words: List[str]
    :type s: str
    :rtype: bool
    """
    ans = ""
    for i in words:
        ans = ans + i[0]
    return ans == s

print(isAcronym(words = ["alice","bob","charlie"], s = "abc"))