# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 18:52:19 2015

@author: Administrator
"""
def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result
