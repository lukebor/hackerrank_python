#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    distances=0
    for i in range(n):
        c.append(i)
        c.sort()
        if c.index(i)==0:
            dist=abs(c[c.index(i)]-c[c.index(i)+1])
        elif c.index(i)==len(c)-1:
            dist=abs(c[c.index(i)]-c[c.index(i)-1])
        else:
            dist=min(abs(c[c.index(i)]-c[c.index(i)-1]),abs(c[c.index(i)]-c[c.index(i)+1]))
        c.remove(i)
        distances=max(distances,dist)
    return distances
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
