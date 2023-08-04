# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:37:57 2023

@author: priya
"""

def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    sum1 = 0
    dictionaryStones = {}
    for i in stones:
        if i in dictionaryStones:
            dictionaryStones[i] += 1
        else:
            dictionaryStones[i] = 1
    for i in jewels:
        if i in dictionaryStones:
            sum1 = sum1 + dictionaryStones[i]
    return sum1


print(numJewelsInStones("aA", "aAAbbbbb"))