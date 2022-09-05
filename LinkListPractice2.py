# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 22:28:35 2022

@author: priya
"""

class LinkedList:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
        
class LinkList:
    def __init__(self, head=None):
        self.head = head
        
    def insert(self, value):
        node = LinkedList(value)
        if self.head == None:
            self.head = node
            return
        curr = self.head 
        while True:
            if curr.nextNode is None:
                curr.nextNode = node
                break
            curr = curr.nextNode
            
    def printList(self):
        curr = self.head  
        while curr is not None:
            print(curr.value, "->", end= " ")
            curr = curr.nextNode
        print(None)
        
    def removeDups(self):
        set1 = set()
        curr = self.head
        while curr.nextNode is not None:
            if (curr.value in set1):
                curr.nextNode = curr.nextNode.nextNode
            set1.add(curr.value)
            curr = curr.nextNode
            
            
    
l1 = LinkList()
l1.insert(1)
l1.printList()
l1.insert(2)
l1.insert(2)
l1.printList()
l1.insert(3)
l1.insert(3)
l1.printList()
l1.insert(4)
l1.insert(4)
l1.printList()
l1.insert(5)
l1.printList()
l1.removeDups()
l1.printList()
