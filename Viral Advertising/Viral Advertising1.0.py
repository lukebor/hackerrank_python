#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def like_gen(day):
    n=1
    num=5
    yield num
    while n<=day:
        yield (num//2)*3
        n+=1
        num=(num//2)*3
def viralAdvertising(n):
    sum=0
    x=like_gen(n)
    for i in range(n):
        sum+=(next(x)//2)
    return sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
