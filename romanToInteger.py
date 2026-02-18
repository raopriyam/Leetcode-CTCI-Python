# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:31:21 2026

@author: priya
"""

def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    dictionary = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000

    }

    totalSum = 0
    for i in range(len(s)):
        if i+1 < len(s) and dictionary[s[i]] < dictionary[s[i+1]]:
            totalSum -= dictionary[s[i]]
        else:
            totalSum += dictionary[s[i]]

    return totalSum

    