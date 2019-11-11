#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_score=max_score=scores[0]
    r_min=r_max=0
    res=[]
    for i in scores:
        if i < min_score:
            r_min+=1
            min_score=i
        if i > max_score:
            r_max+=1
            max_score=i
    res.append(r_max)
    res.append(r_min)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
