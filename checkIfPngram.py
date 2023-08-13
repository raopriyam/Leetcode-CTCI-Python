# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:44:06 2023

@author: priya
"""

def checkIfPangram( sentence):
    """
    :type sentence: str
    :rtype: bool
    """
    set1 = set(sentence)
    return len(set1) == 26

print(checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))