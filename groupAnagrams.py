# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 14:13:42 2026

@author: priya
"""
from collections import defaultdict

def groupAnagrams(strs):
    anagram_dict = defaultdict(list)
    for i in strs:
        count = [0]*26
        for s in i:
            count[(ord(s) - ord('a'))] += 1

        key = tuple(count)

        anagram_dict[key].append(i)

    return anagram_dict.values()