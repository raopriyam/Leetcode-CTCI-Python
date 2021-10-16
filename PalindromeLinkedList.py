# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 22:41:22 2021

@author: priya
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None   
        
    def palindrome(self):
        strcheck = ""
        strcheck2 = ""
        current = self.head
        while current != None:
            strcheck = strcheck + str(current.val)
            strcheck2 = str(current.val) + strcheck2
            current = current.next
        print(strcheck)
        print(strcheck2)
        print()
        print()
        if strcheck == strcheck2:
            print("Palindrome")
        else:
            print("Not Palindrome")
            
list1 = LinkedList()
list1.head = Node(1)
e2 = Node(2)
list1.head.next = e2
e3 = Node(1)
e2.next = e3
list1.palindrome()

list2 = LinkedList()
list2.head = Node(2)
l2 = Node(5)
list2.head.next = l2
l3 = Node(3)
l2.next = l3
list2.palindrome()