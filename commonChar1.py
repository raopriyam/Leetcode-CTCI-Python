# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 22:37:12 2023

@author: priya
"""

def commonChars(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    temp = "".join(words)
    dict1 = {}
    ans = []
    for i in temp:
        if i not in dict1:
            dict1[i] = 1
        elif i in dict1:
            dict1[i] += 1
    print(temp)
    for i in dict1:
        if dict1[i] == len(words):
            ans.append(i)
        print(ans)
    return ans

print(commonChars(["bella","label","roller"]))