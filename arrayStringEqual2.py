# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:31:41 2023

@author: priya
"""

def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    check = "".join(word1)
    check2 = "".join(word2)
    return check == check2

print(arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))