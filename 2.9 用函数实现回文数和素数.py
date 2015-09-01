# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 19:55:39 2015

@author: Administrator
"""
num=131

def is_palin(num):
    num_p=0
    num_t=num
    
    while num!=0:
        num_p=num_p*10+num%10
        num=num/10

    if num_t ==num_p:
        return True
    else:
        return False

def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

if is_palin(num) and is_prime(num):
    print 'Yes'
else:
    print 'No'