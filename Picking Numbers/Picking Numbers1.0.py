#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    solution=[]
    for i in a:
        solution.append(a.count(i)+a.count(i+1))
        solution.append(a.count(i)-a.count(i+1))
    return max(solution)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
