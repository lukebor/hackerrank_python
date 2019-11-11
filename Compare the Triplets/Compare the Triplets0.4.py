#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    c=[0,0]
    for i in range(len(a)):
        if a[i]>b[i]: c[0]+=1
        if a[i]<b[1]: c[1]+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
