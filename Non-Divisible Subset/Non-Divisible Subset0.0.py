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
    result+=arr[0]*(arr[0]-1)//2
    for i in range(1,k):
        if i<(k-i):
            result+=arr[i]*arr[k-i]
        if i==k-i:
            result+=arr[i]*(arr[i]-1)//2
            
    print(result)
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
