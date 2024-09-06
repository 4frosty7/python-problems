# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:35:59 2024

@author: apatb
"""

def solution(a):
    i = 0
    result = [0,0]
    print("a")
    while i < len(a):
        if i%2==0:
            result[0]=result[0]+a[i]
            i=i+1
            continue
        result[1]=result[1]+a[i]
        i = i+1
        print(i)
    return result

a = [50, 60, 60, 45, 70]            
solution(a)