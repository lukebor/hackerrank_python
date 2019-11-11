#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r, c, obstacles):
    result=0
    o1=o2=o3=o4=o5=o6=o7=o8=[n+1,n+1]
    for i in obstacles:
        if i[0]==r and i[1]>c:
            o1=[r,min(i[1]-c,o1[1])]
        if i[0]==r and i[1]<c:
            o2=[r,min(c-i[1],o2[1])]
        if i[1]==c and i[0]>r:
            o3=[min(i[0]-r,o3[0]),c]
        if i[1]==c and i[0]<r:
            o4=[min(r-i[0],o4[0]),c]
        if i[0]>r and i[1]>c and i[0]-r==i[1]-c:
            o5=[min(i[0]-r,o5[0]),min(i[1]-c,o5[1])]
        if i[0]>r and i[1]<c and i[0]-r==c-i[1]:
            o6=[min(i[0]-r,o6[0]),min(c-i[1],o6[1])]   
        if i[0]<r and i[1]<c and r-i[0]==c-i[1]:
            o7=[min(r-i[0],o7[0]),min(c-i[1],o7[1])] 
        if i[0]<r and i[1]>c and r-i[0]==i[1]-c:
            o8=[min(r-i[0],o8[0]),min(i[1]-c,o8[1])]  
    obstacles=[]
    if o1!=[n+1,n+1]:
        o1=[r,c+o1[1]]
        result+=o1[1]-c-1
    else: result+=n-c
    if o2!=[n+1,n+1]:
        o2=[r,c-o2[1]]
        result+=c-o2[1]-1
    else: result+=c-1
    if o3!=[n+1,n+1]:
        o3=[r+o3[0],c]
        result+=o3[0]-r-1
    else: result+=n-r
    if o4!=[n+1,n+1]:
        o4=[r-o4[0],c]
        result+=r-o4[0]-1
    else: result+=r-1
    if o5!=[n+1,n+1]:
        o5=[r+o5[0],c+o5[1]]
        result+=o5[0]-r-1
    else: result+=min(n-c,n-r)
    if o6!=[n+1,n+1]:
        o6=[r+o6[0],c-o6[1]]
        result+=o5[0]-r-1
    else: result+=min(n-r,c-1)
    if o7!=[n+1,n+1]:
        o7=[r-o7[0],c-o7[1]]
        result+=r-o7[0]-1
    else: result+=min(r-1,c-1)
    if o8!=[n+1,n+1]:
        o8=[r-o8[0],c+o8[1]]
        result+=r-o8[0]-1
    else: result+=min(n-c,r-1)
    return result

    
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
