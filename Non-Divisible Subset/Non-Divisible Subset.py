#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    result=0
    arr=[0]*k
    for nums in S:
        arr[nums%k]+=1
    result=min(arr[0],1)
    for i in range(1,k//2+1):
        if i<(k-i):
            result+=max(arr[i],arr[k-i])
        if i==k-i and arr[i]>0:
            result+=1
            

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
