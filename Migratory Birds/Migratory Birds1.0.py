#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(ar):
    a=[]
    for i in range(1,6):
        a.append(ar.count(i))
    return a.index(max(a))+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
