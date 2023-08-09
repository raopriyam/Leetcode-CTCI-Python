# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:51:26 2023

@author: priya
"""

def truncateSentence(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    ans1 = s.split()
    print(ans1)
    return " ".join(ans1[:k])

print(truncateSentence(s = "Hello how are you Contestant", k = 4))