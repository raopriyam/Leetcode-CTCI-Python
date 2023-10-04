# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:15:16 2023

@author: priya
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            return set(s) == set(t)
        return False
    
ob1 = Solution()
output = ob1.isAnagram(s = "anagram", t = "nagaram")

assert output == True
print(output)