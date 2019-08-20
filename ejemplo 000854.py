#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:40:28 2019

@author: agds
"""

b=["banana", "apple", "microsoft"]
print (b)
temp = b[0]
b[0] = b[2]
b[2] = temp
print (b)
b[0],b[2] = b[2],b[0]
print (b)