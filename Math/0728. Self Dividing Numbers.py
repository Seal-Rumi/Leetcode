# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:39:45 2023

@author: Seal-Rumi
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for i in range(left, right+1):
            digit = [int(j) for j in str(i)]
            check = 0
            for j in digit:
                if j==0:
                    check=1
                    break
                if i%j!=0:
                    check =1
            if check==0:
                output.append(i)
        return output