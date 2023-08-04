# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:39:57 2023

@author: priya
"""

def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    sum1 = 0
    for i in jewels:
        sum1 = sum1 + stones.count(i)
    return sum1

print(numJewelsInStones("aA", "aAAbbbbb"))