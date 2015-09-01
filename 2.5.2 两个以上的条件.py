# -*- coding: utf-8 -*-
"""
Created on Sat Feb 07 11:44:21 2015

@author: Administrator
"""
#当所有条件都为真的时候，if成立
age=float(raw_input("Enter your age:"))
grade=int(raw_input("Enter your grade:"))
color=raw_input("Enter your favorite color:")
if age >=8 and grade >=3 and color=="green":
    print "you are allowed to play this game."
else:
    print "Sorry,you can't play the game."