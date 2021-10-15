# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:56:33 2021

@author: priya
"""


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def partition(self,n):
        d1 = c1 = LinkedList()
        d2 = c2 = LinkedList()
        head = self.head
        while head:
            if head.val < n:
                c1.next = head
                c1 = c1.next
            else:
                c2.next = head
                c2 = c2.next
            
            head = head.next
        c2.next = None
        c1.next = d2.next
    def printList(self):
        current = self.head
        while current != None:
            print(current.val)
            current = current.next
    
list1 = LinkedList()
list1.head = Node(0)
e2 = Node(2)
list1.head.next = e2
e3 = Node(4)
e2.next = e3
e4 = Node(1)
e3.next = e4
e5 = Node(3)
e4.next = e5
e6 = Node(5)
e5.next = e6
e7 = Node(6)
e6.next = e7
e8 = Node(1)
e7.next = e8
e9 = Node(2)
e8.next = e9
e10 = Node(5)
e9.next = e10

list1.partition(3)
list1.printList()
        
            
            
            
        
        
    