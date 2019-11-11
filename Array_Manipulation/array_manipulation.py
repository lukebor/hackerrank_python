#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    maxres=0
    sol=0
    res=[0]*(n+1)
    for i in queries:
        res[i[0]-1]+=i[2]
        res[i[1]]-=i[2]
    for i in res:
        sol+=i
        if sol>maxres: maxres=sol
    return maxres
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
