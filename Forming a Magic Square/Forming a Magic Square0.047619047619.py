#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    return abs(s[0][0]+s[2][2]-10)+abs(s[0][1]+s[2][1]-10)+abs(s[0][2]+s[2][0]-10)+abs(s[1][0]+s[1][2]-10)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
