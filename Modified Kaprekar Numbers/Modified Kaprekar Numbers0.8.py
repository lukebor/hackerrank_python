#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    for i in range(p,q+1):
        x=str(i**2)
        y=x[:len(x)-len(str(i))]
        z=x[len(x)-len(str(i)):]
        if y=='':y='0'
        if z=='':z='0'
        if int(y)+int(z)==i:
            print(i, end=' ')

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
