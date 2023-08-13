# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:50:38 2023

@author: priya
"""

def sortPeople(names, heights):
    """
    :type names: List[str]
    :type heights: List[int]
    :rtype: List[str]
    """
    dict1 = {}
    ans = []
    for i in range(len(names)):
        dict1[heights[i]] = names[i]
    heights.sort()
    for i in heights[::-1]:
        ans.append(dict1[i])
    return ans

print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))