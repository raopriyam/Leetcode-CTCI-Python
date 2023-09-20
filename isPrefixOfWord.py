# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:44:55 2023

@author: priya
"""

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        index = 0
        if sentence == None or sentence == []:
            return -1
        else:
            leng = len(searchWord)
            sentencesArray = sentence.split(" ")
            for i in sentencesArray:
                if i[0:leng] == searchWord:
                    return index + 1
                index += 1
            return -1