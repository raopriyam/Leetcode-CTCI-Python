# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:34:31 2021

@author: priya
"""

def accessSubKeyInDict(dict1):
    return dict1["class"]["student"]["marks"]["history"]

print(accessSubKeyInDict({ 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}))