# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:47:36 2023

@author: Seal-Rumi
"""

class Solution:
    def interpret(self, command: str) -> str:
        output = ""
        for i in range(len(command)):
            if command[i]=="(" and command[i+1]==")":
                output += "o"
                continue
            elif command[i]=="(" or command[i]==")":
                continue
            else:
                output += command[i]
        return output