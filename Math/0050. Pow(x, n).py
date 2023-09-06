# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:26:37 2023

@author: Seal-Rumi
"""
import math

#The most simplest version
def myPow(x, n):
    return math.pow(x, n)

#This version is simple but has some issue. For example, time limit exceeded.
def myPow(x, n):
    res = 1
    for i in range(abs(n)):
        res *= x
    if n > 0:
        return res
    else:
        return 1/res

class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        # Base case, to stop recursive calls.
        if n == 0:
            return 1
       
        # Handle case where, n < 0.
        if n < 0:
            return 1.0 / self.binaryExp(x, -1 * n)
       
        # Perform Binary Exponentiation.
        # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
        else:
            return self.binaryExp(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)

#Complicated version
'''
def myPow(x, n):
    sign = x>=0
    unsign_x = abs(x)
    if unsign_x==1:
        if sign:
            return 1
        elif n%2:
            return -1
        else:
            return 1
    # x = (sign) a*10^b
    a, b = x, 1
    if a
'''
      
#Test
x = float(input())
n = int(input())
print(myPow(x, n))
