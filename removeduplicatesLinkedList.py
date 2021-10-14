# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:48:54 2021

@author: priya
"""

class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class SLinklist:
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while (temp ):
            print(temp.val)
            temp = temp.next       
    def removeDuplicates(self,head):
        dict1 = {}
        count = 1
        current = head
        prev = head
        while current != None:
            if current.val in dict1:
                prev.next = current.next
                current = current.next
            else:
                dict1[current.val] = count
                prev = current
                current = current.next
        return head   
    
        
        
list1 = SLinklist()
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


list1.printList()
list1.removeDuplicates(list1.head)
print()
list1.printList()
