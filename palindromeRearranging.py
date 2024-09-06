# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:18:04 2024

@author: apatb
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""
def solution (a):
    inputParity = len(a)%2
    parityCheck = 0
    characterParity = {}
    for i in a:
        if i not in characterParity:
            characterParity[i] = 1
            continue
        characterParity[i] = characterParity[i]+1
    for i in characterParity:
        characterParity[i] = characterParity[i]%2
        parityCheck = parityCheck + characterParity[i]
    if inputParity == parityCheck:
        return True
    return False
inputString = "aabb"
solution (inputString)
