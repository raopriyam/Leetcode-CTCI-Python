# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:33:15 2023

@author: priya
"""

def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    return "".join(word1) == "".join(word2)

print(arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))