# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:42:21 2023

@author: priya
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        listS = list(s)
        listT = list(t)
        listS.sort()
        listT.sort()
        return listS == listT
    
ob1 = Solution()
output = ob1.isAnagram(s = "anagram", t = "nagaram")

assert output == True
print(output)