# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 20:24:20 2026

@author: priya
"""

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    paragraph = paragraph.lower()
    for ch in "!?',;.":
        paragraph = paragraph.replace(ch, " ")

    s = paragraph.split()
    dictionary = {}
    bannedset = set(banned)
    maxcount = 0
    ans = ""

    for i in s:
        if i in bannedset:
            continue

        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1

        if dictionary[i] > maxcount:
            maxcount = dictionary[i]
            ans = i

    return ans
 
    

