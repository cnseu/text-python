# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 17:29:09 2015

@author: Administrator
"""

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 