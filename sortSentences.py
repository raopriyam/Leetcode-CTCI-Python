# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:27:31 2023

@author: priya
"""

def sortSentence( s):
    """
    :type s: str
    :rtype: str
    """
    temp = s.split(" ")
    leng = len(temp)
    ans = ["a"]*leng
    for i in temp:
        k = len(i)-1
        ans[int(i[-1])-1] = i[:k]
    return " ".join(ans)

print(sortSentence(s = "is2 sentence4 This1 a3"))