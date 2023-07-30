# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 23:17:23 2023

@author: priya
"""

def mostWordsFound(sentences):
    """
    :type sentences: List[str]
    :rtype: int
    """
    ans = []
    for i in sentences:
        temp1 = i.split(" ")
        ans.append(len(temp1))
    return max(ans)

print(mostWordsFound(["my name is priyam","who are you?","i don't know wether or not you will be able to beat me"]))
