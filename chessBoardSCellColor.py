# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 06:59:04 2024

@author: apatb
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.



For cell1 = "A1" and cell2 = "H3", the output should be
solution(cell1, cell2) = false.



Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string cell1

Guaranteed constraints:
cell1.length = 2,
'A' ≤ cell1[0] ≤ 'H',
1 ≤ cell1[1] ≤ 8.

[input] string cell2

Guaranteed constraints:
cell2.length = 2,
'A' ≤ cell2[0] ≤ 'H',
1 ≤ cell2[1] ≤ 8.

[output] boolean

true if both cells have the same color, false otherwise.
"""
import string
def solution (a,b):
    c= string.ascii_uppercase
    convertedA = [c.index(a[0])%2,int(a[1])%2]
    convertedB = [c.index(b[0])%2,int(b[1])%2]
    convertedA = (convertedA[0]-convertedA[1])**2
    convertedB = (convertedB[0]-convertedB[1])**2
    return convertedA==convertedB
pairing = ['A1','C3']
solution(pairing[0],pairing[1])

