#!/bin/python3

import os
import sys
from fractions import gcd
#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    x=a[0]
    y=b[0]
    res=0
    if len(a)>1:
        for i in range(1,len(a)):
            x=int((x*a[i])/(gcd(x,a[i])))
    if len(b)>1:
        for i in range(1,len(b)):
            y=gcd(y,b[i])
            print(y)
    for i in range(x,y+1,x):
        if not y%i:
            res+=1
    return res
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
