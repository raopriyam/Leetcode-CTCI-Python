# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:42:54 2023

@author: priya
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        listS = []
        for i in s:
            listS.append(str(i))
        for i in t:
            listS.remove(str(i))
        return listS  == []
    
ob1 = Solution()
output = ob1.isAnagram(s = "anagram", t = "nagaram")

assert output == True
print(output)
