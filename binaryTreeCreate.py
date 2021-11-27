# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 23:36:55 2021

@author: priya
"""

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = Node(10)
root.PrintTree()