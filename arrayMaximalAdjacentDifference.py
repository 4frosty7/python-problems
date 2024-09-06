# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:56:43 2024

@author: apatb

Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 10,
-15 ≤ inputArray[i] ≤ 15.

[output] integer

The maximal absolute difference.
"""

def solution(inputArray):
    absDiff = None
    for i in range(len(inputArray)-1):
        temp = abs(inputArray[i]-inputArray[i+1])
        if i == 0:
            absDiff = temp
            continue
        if absDiff < temp:
            absDiff = temp
    return absDiff
inputArray = [2, 4, 1, 0]
solution(inputArray)