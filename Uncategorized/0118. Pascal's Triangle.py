# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:32:33 2023

@author: Seal-Rumi
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1, numRows):
            tempRow = [1]
            for j in range(1,i):
                tempRow.append(output[i-1][j-1]+output[i-1][j])
            tempRow.append(1)
            output.append(tempRow)
        return output