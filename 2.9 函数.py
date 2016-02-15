# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 17:57:33 2015

@author: Administrator
"""

def iterativePower(x, p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
        return result
        