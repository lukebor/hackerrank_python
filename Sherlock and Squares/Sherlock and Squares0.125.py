#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    result=0
    if a**0.5==math.floor(a**0.5):
        result+=1
    if b**0.5==math.floor(b**0.5):
        result+=1
    result+=math.floor(b**0.5)-math.floor(a**0.5)-1
    if result < 0:
        return 0
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
