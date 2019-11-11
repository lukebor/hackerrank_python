#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    result=0
    f1,f2,f3,f4,f5,f6,f7,f8=0,0,0,0,0,0,0,0
    for i in range(n):
        if [r_q+i,c_q] not in obstacles:
            if r_q+i<=n and f7==0: result+=1
        else: f7=1
        if [r_q-i,c_q] not in obstacles:
            if r_q-i>0 and f8==0: result+=1
        else: f8=1
        if [r_q,c_q+i] not in obstacles:
            if c_q+i<=n and f5==0: result+=1
        else: f5=1
        if [r_q,c_q-i] not in obstacles:
            if c_q-i>0 and f6==0: result+=1
        else: f6=1
        if [r_q+i,c_q+i] not in obstacles:
            if r_q+i<=n and c_q+i<=n and f1==0: result+=1
        else: f1=1
        if [r_q+i,c_q-i] not in obstacles:
            if r_q+i<=n and c_q-i>0 and f2==0: result+=1
        else: f2=1
        if [r_q-i,c_q+i] not in obstacles:
            if r_q-i>0 and c_q+i<=n and f3==0: result+=1
        else: f3=1
        if [r_q-i,c_q-i] not in obstacles:
            if r_q-i>0 and c_q-i>0 and f4==0: result+=1
        else: f4=1
    return result-8
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()