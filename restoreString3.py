# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 23:16:50 2023

@author: priya
"""

def restoreString( s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    ans = ""
    for i in range(len(s)):
        ans = ans + s[indices.index(i)]
    return ans

print(restoreString("codeleet", indices = [4,5,6,7,0,2,1,3]))