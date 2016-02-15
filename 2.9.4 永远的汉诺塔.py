# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 10:25:00 2015

@author: Administrator
"""
count=0

def han(n,A,B,C):
    global count    
    if n ==1:
        print 'Move disk',n,'form',A,'to',C
        count +=1
    else:
        han(n-1,A,C,B)
        print 'Move disk' ,n,'form',A,'to',C
        count +=1        
        han(n-1,B,A,C)

n=int(raw_input("Please input a number:"))
han(n,'Left','Mid','Right')
print count