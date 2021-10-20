# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:40:20 2021

@author: priya
"""

def sortFunc(list1):
    list1.sort()
    return list1


        

def QuickSort(list1):
    i = 1
    while i<len(list1):
        if list1[i]<list1[i-1]:
            temp1 = list1[i]
            list1[i] = list1[i-1]
            list1[i-1] = temp1
                
        j = i
        while( j>0):
            if list1[j]<list1[j-1]:
                temp = list1[j]
                list1[j] = list1[j-1]
                list1[j-1] = temp
            j = j - 1
        i += 1
    return list1

def sortUsingMin(list1):
    i = 0
    while i <len(list1):
        a = min(list1[i:])
        list1.remove(a)
        list1.insert(i,a)
        i = i +1
    return list1
        
        #print(list1[i])
print(sortFunc([3,2,5,4,1,6]))
print(QuickSort([3,2,9,0,-10,87,4,1,6]))
print(sortUsingMin([3,2,5,4,1,6]))
        
