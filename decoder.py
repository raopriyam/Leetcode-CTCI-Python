# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:55:59 2021

@author: priya
"""

def decoder(s):
    i = 0
    n = len(s)
    ans = [0]*26
    while i<n:
        if i+2<len(s)and s[i+2] == "#":
            ans[int(s[i:i+2])-1] = ans[int(s[i:i+2])-1] +1
            i = i+2
            #print(ans[int(s[i:i+2])])
                
            print()
        else:
            if s[i+1] == "(":
                j = i
                check = ""
                while(s[j+1] != ")"):
                    check = check + s[j]
                    j = j+1
                ans[int(s[i])-1] = ans[int(s[i])-1] + int(check)
                
            ans[int(s[i])-1] = ans[int(s[i])-1] + 1
            
        i = i+1
    return ans
        
        
print(decoder("1(3)27613#977221#"))