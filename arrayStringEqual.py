# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:29:30 2023

@author: priya
"""

def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    concate1 = "" 
    concate2 = ""
    for i in word1:
        concate1 = concate1 + i
    for i in word2:
        concate2 = concate2 + i
    return concate1 == concate2

print(arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))