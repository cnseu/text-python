# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 10:49:41 2015

@author: Administrator
"""

x = 12345
epsilon = 0.01  #表示距离答案还有多远
numGuesses = 0
low = 0.0  #一大一小两个数
high = x
ans = (high + low)/2.0  #中间值
while abs(ans**2 - x) >= epsilon:   #正确，远
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))