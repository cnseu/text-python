# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 21:05:28 2015

@author: Administrator
"""

def a(price,tax_rate):
        total=price + (price*tax_rate)
        return total
my_price=float(raw_input("Enter a price"))    
totalPrice=a(my_price,0.06)
print"price=",my_price,"Total price=",a    