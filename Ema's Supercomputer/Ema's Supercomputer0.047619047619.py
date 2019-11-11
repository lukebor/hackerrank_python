#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def checksize(arr,r,c):
    size=1
    arr[r]=arr[r][:c]+'B'+arr[r][(c+1):]
    for i in range(1,min(r,n-r-1,c,m-c-1)+1):
        if arr[r][i+c]==arr[r][c-i]==arr[r-i][c]==arr[r-i][c]=='G':
            if i:
                size+=4
                arr[r]=arr[r][:(c+i)]+'B'+arr[r][(c+i+1):]
                arr[r]=arr[r][:(c-i)]+'B'+arr[r][(c-i+1):]
                arr[r-i]=arr[r-i][:c]+'B'+arr[r-i][(c+1):]
                arr[r+i]=arr[r+i][:c]+'B'+arr[r+i][(c+1):]

        else: break
    return size
def twoPluses(grid):
    pluses=(0,0)
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='G':
                print(i,j)
                temp=checksize(grid,i,j)
                print(temp)
                if temp>pluses[0]:
                    pluses=(temp,pluses[0])
                elif temp>pluses[1]:
                    pluses=(pluses[0],temp)
                else: pass
    return pluses[0]*pluses[1]

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
