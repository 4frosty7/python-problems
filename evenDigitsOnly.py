# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 06:20:55 2024

@author: apatb
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.
"""
def solution (n):
    n = str(n)
    digits = {int(i) for i in n}
    for i in digits:
        isEven = i%2
        if isEven == 1: return False
    return True
n = 248622
solution (n)