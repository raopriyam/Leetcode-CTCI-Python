# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:43:31 2021

@author: priya
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
        
    
    def kthLast(self,k):
        count = 0
        current = self.head
        while current != None:
            current = current.next
            count += 1
        current = self.head
        for i in range(count - k):
            current = current.next
        print(current.val)
        
list1 = LinkedList()
list1.head = Node(2)
e2 = Node(2)
list1.head.next = e2
e3 = Node(2)
e2.next = e3
e4 = Node(2)
e3.next = e4
e5 = Node(2)
e4.next = e5
e6 = Node(2)
e5.next = e6
e7 = Node(2)
e6.next = e7
e8 = Node(3)
e7.next = e8
e9 = Node(4)
e8.next = e9
e10 = Node(5)
e9.next = e10


list1.kthLast(2)