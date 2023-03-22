# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:29:09 2023

@author: priya
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 