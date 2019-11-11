#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def oddity(n):
    return n%2
def fairRations(B):
    result=0
    ind=[]
    odds=list(map(oddity, B))
    print(odds)
    if oddity(sum(odds)): return 'NO'
    else:
        for i in range(len(odds)):
            if odds[i]: ind.append(i)
        ind.sort()
    for i in range(0,len(ind),2):
        result+=(ind[i+1]-ind[i])*2
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
