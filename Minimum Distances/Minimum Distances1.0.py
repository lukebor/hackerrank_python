#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    d=0
    for i in a:
        if a.count(i)>1:
            if not d:
                d=abs(a.index(i,a.index(i)+1)-a.index(i))
            else: d=min(d,abs(a.index(i,a.index(i)+1)-a.index(i)))
    if not d: return -1
    else: return d
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
