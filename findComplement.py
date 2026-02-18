# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:33:14 2026

@author: priya
"""

def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    binary = bin(num)[2:]
    ans = ""
    for i in binary:
        if i == '1':
            ans += '0'
        else:
            ans += '1'

    return int(ans,2)
