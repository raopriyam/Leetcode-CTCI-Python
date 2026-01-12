# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 22:17:01 2026

@author: priya
"""

def sumDifference(queries):
    array1 = [4,2,1,7,5]
    ans = []
    for j in queries:
        oddsum = 0
        evensum = 0
        for i in range(j[0],j[1]+1):
            if i%2 == 0:
                if array1[i] < 0:
                    pass
                else:
                    evensum = evensum + array1[i]
            else:
                if array1[i] < 0:
                    pass
                else:
                    oddsum = oddsum + array1[i]
            
        ans.append(evensum - oddsum)
    return ans
            

print(sumDifference([[0,3],[1,4]]))

