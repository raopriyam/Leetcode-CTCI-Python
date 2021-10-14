# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:06:49 2021

@author: priya
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printlist(self):
 
        temp = self.head
 
        while (temp):
            print(temp.val)
            temp = temp.next
        print()
        print()

    def deleteMiddleNode(self,n):
        current = self.head
        count = 0
        prev = self.head
        while current != None:
            if count == n:
                prev.next = current.next
                current = current.next
            print(current.val)
            current = current.next
            count = count +1
            
            
            
list1 = LinkedList()
list1.head = Node(1)
e2 = Node(2)
list1.head.next = e2
e3 = Node(3)
e2.next = e3
e4 = Node(4)
e3.next = e4
e5 = Node(5)
e4.next = e5
e6 = Node(6)
e5.next = e6
e7 = Node(7)
e6.next = e7
e8 = Node(8)
e7.next = e8
e9 = Node(9)
e8.next = e9
e10 = Node(10)
e9.next = e10

list1.printlist()
list1.deleteMiddleNode(3)