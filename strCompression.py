# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:08:56 2021

@author: priya
"""

"""aaabcccccdddaab """ """ a3b1c5d3a2b1"""

def strCompress(s):
    ans = ""
    i = 0
    count = 1
   
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            ans = ans + s[i] + str(count)
            print(ans)
            count = 1
        
    ans = ans +s[i]+ str(count)  
    print(ans)

strCompress("aaabcccccdddaabbb")
        
            
            