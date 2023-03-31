# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 22:18:01 2023

@author: priya
"""
def dateDifference(date1, date2):
    list1 = date1.split("/")
    list2 = date2.split("/")
    days = 0
    count = 0
    for i in range(len(list1)):
        if count == 0:
            days = days + (int(list2[i]) - int(list1[i]))*365
            count += 1
        elif count == 1:
            days = days + (int(list2[i]) - int(list1[i]))*30
            count += 1 
        else:
            days = days + (int(list2[i]) - int(list1[i]))

    return days


print(dateDifference("2023/02/27", "2023/03/30"))
    