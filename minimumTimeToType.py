# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:34:21 2026

@author: priya
"""

def minTimeToType(self, word):
    """
    :type word: str
    :rtype: int
    """
    total = len(word) 
    startVal = 0
    for i in word:
        tempVal = ord(i) - 97
        diff = abs(tempVal - startVal)
        total +=  min(diff,26-diff)
        startVal = tempVal

    return total
    