#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def checkcommon(arr1,arr2,a,b):
    set1=[(arr1[1],arr1[2])]
    for i in range(1,((arr1[0]-4*a)//4)+1):
        set1.append((arr1[1],arr1[2]+i))
        set1.append((arr1[1],arr1[2]-i))
        set1.append((arr1[1]-i,arr1[2]))
        set1.append((arr1[1]+i,arr1[2]))
    print(set1)
    for i in range(1,((arr2[0]-4*b)//4)+1):
        if (arr2[1],arr2[2]) in set1: return False
        if (arr2[1]+i,arr2[2]) in set1: return False
        if (arr2[1]-i,arr2[2]) in set1: return False
        if (arr2[1],arr2[2]+i) in set1: return False
        if (arr2[1],arr2[2]-i) in set1: return False
    return True
        
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
            for i in range(pluses[k][0]//4+1):
                for j in range(pluses[l][0]//4+1):
                    if (pluses[k][0]-4*i)*(pluses[l][0]-4*j)>result:
                        if checkcommon(pluses[k],pluses[l],i,j):
                            result=(pluses[k][0]-4*i)*(pluses[l][0]-4*j)
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
