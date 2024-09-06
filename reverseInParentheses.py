# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 01:44:13 2024

@author: apatb
"""

'''
reverses characters

within parentheses

find open parenthesis index and put in list
find close parenthesis index and put in list

priority: first in last out
reverse open parenthesis list and pair with close parenthesis


'''
def ToList(inputString):
    a = []
    for i in inputString:
        a.append(i)
    return a


def solution(a):
    inputString = ToList(a)
    outputList = []
    outputString = ""
    level = 0
    levelIndex = []
    highestLvl = 0
    for i in inputString:
        if i == "(":
            level = level+1
            if level > highestLvl: highestLvl = level
        if i == ")":
            level = level-1
        levelIndex.append(level)
    while highestLvl > 0:
        print ("highestLvl = ", highestLvl)
        i=0
        while i < len(inputString): #iterating throughout the list
            #j=i
            if levelIndex[i]<highestLvl:
                outputList.append(inputString[i])
                i=i+1
                continue
            tempReverse = []
            while levelIndex[i] == highestLvl: #reach the deepest level
                levelIndex[i] = levelIndex[i]-1 #decrease levelIndex by 1
                tempReverse.append(inputString[i]) #append
                i=i+1
            tempReverse = tempReverse[::-1] #reverse the temp
            for k in tempReverse:
                outputList.append(k)
        print(outputList)
        inputString = outputList
        outputList = []
        highestLvl = highestLvl-1
    
    for i in inputString:
        if i in ["(",")"]:continue
        outputString = outputString + i
    return(outputString)
    
inputString = "(b(ar)n)"
#inputString = "foo(bar(bazj))b(lim)"
solution(inputString)

