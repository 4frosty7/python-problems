# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:37:31 2024

@author: apatb
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.boolean matrix

A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains a mine, false otherwise.

Guaranteed constraints:
2 ≤ matrix.length ≤ 100,
2 ≤ matrix[0].length ≤ 100.

[output] array.array.integer

Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.
"""

def solution(matrix):
    #expanding the matrix
    tempMatrix = [[0]*(len(matrix[0])+2) for i in range (len(matrix)+2)]
    expandedMatrix = [[0]*(len(matrix[0])+2) for i in range (len(matrix)+2)]
    
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            expandedMatrix[i+1][j+1] = matrix[i][j]

    for i in range (len(expandedMatrix)-1):
        row = expandedMatrix[i]
        if True not in row:
            continue
        
        for j in range(len(row)):
            if row[j] != True: continue
            for a in range(-1,2):
                for b in range (-1,2):
                    if a==0 and b == 0:
                        continue
                    tempMatrix[i+a][j+b] = tempMatrix[i+a][j+b]+1
    output = tempMatrix[1:len(tempMatrix)-1]
    for i in output:
        i.pop(0)
        i.pop(-1)
    return output

matrix = [[True,False,False,True], 
          [False,False,True,False], 
          [True,True,False,True]]

solution(matrix)
#finished September 8, 2024