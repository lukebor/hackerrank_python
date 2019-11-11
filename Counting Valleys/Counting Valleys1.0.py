#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys=0
    height=0
    v_ready=1
    for i in s:
        if i=='U': height+=1
        else: height-=1
        if height==0: v_ready=1
        if height==-1 and v_ready==1: 
            valleys+=1
            v_ready=0
    return valleys
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
