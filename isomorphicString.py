# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:38:12 2022

@author: priya
"""

def isomorphicString(s1,s2):
    dict1 = {}
    if len(s1) != len(s2):
        return False
    if len(set(s1)) != len(set(s2)):
        return False
    for i in range(len(s1)):
        if s1[i] not in dict1:
            dict1[s1[i]] = s2[i]
        elif (dict1[s1[i]] != s2[i]):
            return False
    return True
    
print(isomorphicString("egg","add"))


print(isomorphicString("foo",  "bar"))