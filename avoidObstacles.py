# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 02:47:48 2024

@author: apatb
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.

Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer inputArray

Non-empty array of positive integers.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 1000,
1 ≤ inputArray[i] ≤ 1000.

[output] integer

The desired length.
"""
def largest (a):
    largest = 0
    for i in a:
        if largest < i:
            largest = i
    return largest
def solution (a):
    big = largest(a)+10
    for i in range (big):    
        if i < 2: continue
        modList = []
        for j in a:
            b = j%i
            modList.append(b)
            if b == 0: break
        if 0 not in modList: return i
            
inputArray = [5, 3, 6, 7, 9]
solution(inputArray)