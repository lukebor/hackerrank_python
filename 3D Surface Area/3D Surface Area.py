#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    sol=0
    x = [[0] * (len(A[0]) + 2)]
    for i in A:
        x.append([0] + i + [0])
    x.append([0] * (len(A[0]) + 2))

    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j]: sol+=2
    print(x)
    for i in range(1, len(x)-1):
        for j in range(1, len(x[i])-1):
            sol+=max(0,x[i][j]-x[i][j+1])
            sol+=max(0,x[i][j]-x[i][j-1])
            sol+=max(0,x[i][j]-x[i+1][j])
            sol+=max(0,x[i][j]-x[i-1][j])
    return sol
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
