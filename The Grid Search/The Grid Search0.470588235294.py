#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.

def check_grid(n,m):
    if R-n<r: return False
    if C-m<c: return False
    ok=0
    for j in range(r):
        if m+c>=C:
            if G[n+j][m:]==P[j]: ok=1; print(n+j)
        elif G[n+j][m:m+c]==P[j]:
            ok=1;print(m+c)
        else: return False
    return True
    
def gridSearch(G, P):
    for i in G:
        z=0
        if P[0] in i:
            for _ in range(i.count(P[0])):
                if check_grid(G.index(i,z),i.index(P[0])): return 'YES'
                z=G.index(i,z)+1
    return 'NO'
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
