# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 23:12:47 2023

@author: priya
"""

def restoreString( s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    ansdict = {} 
    ans = [0]*len(s)
    check = 0
    for i in indices:
        ans[i]=s[check]
        check += 1
    for i in ansdict:
        ans.append(ansdict[i])
    return "".join(ans)

print(restoreString("codeleet", indices = [4,5,6,7,0,2,1,3]))