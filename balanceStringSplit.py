# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:26:21 2023

@author: priya
"""

def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """
    lcount = 0
    rcount = 0
    check = 0
    for i in s:
        if i == "R":
            rcount += 1
        else:
            lcount += 1
        if (lcount>0) and (lcount == rcount):
            check += 1
    if check > 1:
        return check
    else:
        return 1

print(balancedStringSplit("RLRRLLRLRL"))