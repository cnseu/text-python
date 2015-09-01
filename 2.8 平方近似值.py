# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 10:32:12 2015

@author: Administrator
"""

x = 25
epsilon = 0.01  #代表我希望计算值和真实值的接近程度
step = epsilon**2    #选择步长，从0开始不断增加步长，这里设置为ε的平方
numGuesses = 0      #初始答案为0
ans = 0.0
while (abs(ans**2 - x)) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses = ' + str(numGuesses))
if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))