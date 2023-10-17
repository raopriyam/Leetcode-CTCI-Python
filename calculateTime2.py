# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:38:06 2023

@author: priya
"""

class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        dictionary = {}
        res = 0
        temp = 0
        for i in range(len(keyboard)):
            dictionary[keyboard[i]] = i
    
        for i in word:
            res = res + abs(dictionary[i] - temp)
            temp = dictionary[i]

        return res