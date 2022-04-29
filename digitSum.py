# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:49:46 2022

@author: priya
"""

def digitSum(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    res = []
    count = 0
    for i in range(0,len(s),k):
        if (count+k)<len(s):
            res.append(int(s[i:i+k]))
        else:
            res.append(int(s[i:]))
        count = count+k
    return sum(res)


print(digitSum("11111222223", 3))