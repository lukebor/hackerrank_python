#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    c=[]
    for i in range (0,3):
        if a[i]!=b[i]: c.append(1)
    if sum(c): return c
    else: return None

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
