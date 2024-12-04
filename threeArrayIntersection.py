# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:47:10 2024

@author: priya
"""

def arraysIntersection(self, arr1, arr2, arr3):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :type arr3: List[int]
    :rtype: List[int]
    """
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)
    ans = []

    for i in set1:
        if i in set3 and i in set2:
            ans.append(i)
    ans.sort()
    return ans