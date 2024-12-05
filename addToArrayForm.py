# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:54:11 2024

@author: priya
"""

def addToArrayForm(self, num, k):
    """
    :type num: List[int]
    :type k: int
    :rtype: List[int]
    """
    st1 = ""
    list1 = []
    for i in num:
        st1 = st1 + str(i) 
    res = str(int(st1) + k)

    for i in res:
        list1.append(int(i))
    
    return list1