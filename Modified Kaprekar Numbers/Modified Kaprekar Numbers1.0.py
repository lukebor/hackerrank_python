#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    range_error=1
    for i in range(p,q+1):

        x=str(i**2)
        y=x[:len(x)-len(str(i))]
        z=x[len(x)-len(str(i)):]
        if y=='':y='0'
        if z=='':z='0'
        if int(y)+int(z)==i:
            range_error=0
            print(i, end=' ')
    if range_error: print('INVALID RANGE')
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
