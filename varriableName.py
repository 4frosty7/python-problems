# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 06:31:30 2024

@author: apatb
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;
For name = "qq-q", the output should be
solution(name) = false;
For name = "2w2", the output should be
solution(name) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string name

Guaranteed constraints:
1 ≤ name.length ≤ 10.

[output] boolean

true if name is a correct variable name, false otherwise.
"""
import string
def solution (name):
    digits = [str(i) for i in range(10)]
    if name[0] in digits: return False
    
    chars = {i for i in name}
    allowedChars = ""
    for i in digits:
        allowedChars = allowedChars + i
    allowedChars = allowedChars + string.ascii_lowercase + string.ascii_uppercase+"_"
    for i in chars:
        if i not in allowedChars: return False
    return True

name = "var_1_Int"
solution (name)
