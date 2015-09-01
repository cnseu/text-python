# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 18:58:54 2015

@author: Administrator
"""

x = raw_input('Enter a number: ')
p = int(raw_input('Enter an integer power: '))

result = 1

for turn in range(p):
    print('iteration: ' + str(turn) + ' current result: ' + str(result))
    result = result * x
