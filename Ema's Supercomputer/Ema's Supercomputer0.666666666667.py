#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def checksize(arr,r,c):
    size=1
    for i in range(1,min(r,n-r-1,c,m-c-1)+1):
        if arr[r][i+c]==arr[r][c-i]==arr[r-i][c]==arr[r+i][c]=='G':
            if i:
                size+=4

        else: break
    return size
def twoPluses(grid):
    pluses=[]
    result=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='G':
                temp=checksize(grid,i,j)
                pluses.append([temp,i,j])
    print(pluses)
    print(len(pluses))
    for k in range(len(pluses)):
        for l in range(k+1,len(pluses)):
            if pluses[k][0]*pluses[l][0]>result:
                if abs(pluses[k][1]-pluses[l][1])+abs(pluses[k][2]-pluses[l][2])>pluses[k][0]//4+pluses[l][0]//4:
                    result=pluses[k][0]*pluses[l][0]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
