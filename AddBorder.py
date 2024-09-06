# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:52:41 2024

@author: apatb
"""
def solution(a):
    length = len(a)
    width = len(a[0])
    out = []
    for i in range(length):
        a[i] = "*"+a[i]+"*"
    for i in range(length+2):
        print (i,length+2)
        if i in [0,length+1]:
            out.append((width+2)*"*")
            continue
        out.append(a.pop(0))
    return (out)

picture = ["abc",
           "ded"]
solution(picture)