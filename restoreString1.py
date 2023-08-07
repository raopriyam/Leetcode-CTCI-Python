# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 22:54:23 2023

@author: priya
"""

def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    ans = [0]*len(s)
    check = 0
    for i in indices:
        ans[i]=s[check]
        check += 1
    return "".join(ans)

print(restoreString("codeleet", indices = [4,5,6,7,0,2,1,3]))