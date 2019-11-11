#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.

def check_grid(row,col):
    for x in range(r):
        for y in range(c):
            if G[row+x][col+y]==P[x][y]: pass
            else: return False
    return True
def gridSearch(G, P):
    flag=0
    for i in range(C-c+1):
        for j in range(R-r+1):
            if check_grid(j,i): flag=1
    if flag: return 'YES'
    else: return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
