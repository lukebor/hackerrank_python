#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reversenum(i):
    return int(str(i)[::-1])
def beautifulDays(i, j, k):
    result=0
    for x in range(i,j+1):
        if not abs(x-reversenum(x))%k:
            result+=1
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
