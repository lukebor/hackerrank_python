#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(0,n):
        if i==n-1:
            print('#'*(i+1))
        else: print(' '*(n-i-2),'#'*(i+1))
if __name__ == '__main__':
    n = int(input())

    staircase(n)
