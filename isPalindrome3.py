# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:14:15 2023

@author: priya
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = ""
        for i in s:
            if i.isalnum():
                ans = ans + i.lower()
        return ans == ans[::-1]
    
    
ob1 = Solution()
output = ob1.isPalindrome("A man, a plan, a canal: Panama")

assert output == True
print(output)