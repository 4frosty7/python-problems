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
    output = []
    for i in range (len(matrix)):
        row = []
        for j in range(len(matrix[0])):    
            row.append(0)
        output.append(row)
    #for the inside elements
    for i in range (len(matrix)):
        if i in [0,len(matrix)-1]: continue
        row = matrix[i]
        if True not in row:
            continue
        for j in range(len(row)):
            if j in[0,len(row)-1]: continue 
            for a in range(-1,2):
                for b in range (-1,2):
                    if a==0 and b == 0:
                        continue
                    output[i+a][j+b]= output[i+a][j+b]+1
    #for the left border elements
    leftBorder = [x[0] for x in matrix]
    left
    rB = len(matrix[0])-1
    rightBorder =[x[rB] for x in matrix]
    print(leftBorder,rightBorder)    
    return output
matrix = [[True, False, False],
          [False, True, False],
          [False, True, True],
          [False, False, False]]

solution(matrix)