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
            if i+3 < n and s[i+3] == "(":
                check2 = ""
                temp = int(s[i:i+2])
                i += 4
                while s[i]!= ")":
                    check2 = check2 + s[i] 
                    if i == n-1:
                        pass
                    else:
                        i += 1
                ans[temp-1] = ans[temp-1] + int(check2)
            else:
                ans[int(s[i:i+2])-1] = ans[int(s[i:i+2])-1] +1
                i = i+2
            #print(ans[int(s[i:i+2])])
        elif i+1 < n and s[i+1] == "(":
            temp = int(s[i])
            check = ""
            i = i+2
            while s[i] != ")":
                check = check+s[i]
                i+=1
                
            ans[temp-1] = ans[temp-1] + int(check)
                
            
        else:     
            ans[int(s[i])-1] = ans[int(s[i])-1] + 1
        i = i+1
    return ans
        
        
print(decoder("12(3)7613#977221#(7)"))
print(decoder("1226#24#"))
print(decoder("1(2)23(3)"))
print(decoder("2110#(2)"))
print(decoder("23#(2)24#25#26#23#(3)"))