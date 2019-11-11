#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bombing(t):
    if t<3: return t+1
    return 4
        
def mapper(x):
    return -1 if x=='.' else 1
def revmapper(x):
    return '.' if x==-1 else 'O'
def bomberMan(n, grid):
    
    grid=[list(map(mapper,x)) for x in grid]
    for i in range(2,n+1):
        grid=[list(map(bombing,x)) for x in grid]
        for j in range(r):
            for k in range(c):
                if grid[j][k]==3:
                    try:
                        if grid[j][k-1]!=3 and k>0:
                            grid[j][k-1]=-1
                    except: pass
                    try:
                        if grid[j][k+1]!=3:
                            grid[j][k+1]=-1
                    except: pass
                    try:
                        if grid[j-1][k]!=3 and j>0:
                            grid[j-1][k]=-1
                    except: pass
                    try:
                        if grid[j+1][k]!=3:
                            grid[j+1][k]=-1
                    except: pass
                    try:
                        grid[j][k]=-1
                    except: pass
    grid=[list(map(revmapper,x))for x in grid]
    return grid
                
                    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    for j in range(len(result)):
        fptr.write(''.join(result[j]))
        fptr.write('\n')

    fptr.close()
