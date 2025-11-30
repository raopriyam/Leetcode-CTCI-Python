# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 23:05:04 2025

@author: priya
"""

password = input("Enter a password: ")

strength = 0

if len(password) >= 8:
    strength += 1
if any(c.isdigit() for c in password):
    strength += 1
if any(c.isupper() for c in password):
    strength += 1
if any(c in "!@#$%^&*()_+" for c in password):
    strength += 1

if strength <= 1:
    print("Weak password")
elif strength == 2:
    print("Medium password")
else:
    print("Strong password")
