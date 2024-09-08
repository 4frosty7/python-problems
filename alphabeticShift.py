# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 06:50:57 2024

@author: apatb
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.
"""
import string
def solution (inputString):
    outputString = ""
    indexList = [(string.ascii_lowercase.index(i)+1)%26 for i in inputString]
    for i in indexList:
        outputString = outputString + string.ascii_lowercase[i]
    return outputString
a = "crazy"
solution(a)
