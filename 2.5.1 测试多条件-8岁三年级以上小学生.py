# -*- coding: utf-8 -*-
"""
Created on Sat Feb 07 10:59:36 2015

@author: Administrator
"""
age=float(raw_input(""))
grade=int(raw_input(""))
if age>=8: #if age>=8 and grade>=3 也可以实现
    if grade>=3:
        print"You can play this game"
else:
    print"Sorry,you can't play the game."
