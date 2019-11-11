#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    res=0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[j]<A[i]: res+=1
    return 'NO' if res%2 else 'YES' 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
