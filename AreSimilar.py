# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:19:04 2024

@author: apatb
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer a

Array of integers.

Guaranteed constraints:
3 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.

[input] array.integer b

Array of integers of the same length as a.

Guaranteed constraints:
b.length = a.length,
1 ≤ b[i] ≤ 1000.

[output] boolean

true if a and b are similar, false otherwise.
"""
def solution (a,b):
    diff = 0
    swappable = []
    for i in range (len(a)):
        if a[i]!=b[i]:
            diff = diff +1
            swappable.append([a[i],b[i]])
        if diff > 2:
            return False
    if diff == 0:
        return True
    if diff == 1:
        return False
    if diff == 2:
        return swappable[0][0] == swappable[1][1] and swappable[0][1] == swappable[1][0]    
    
a = [1,2,3]
b = [2,1,3]
solution (a,b)
