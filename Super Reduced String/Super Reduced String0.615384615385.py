#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    res=''
    for i in s:
        if s.count(i) % 2 != 0 and i not in res:
            res+=i
    return res if len(res)>0 else 'Empty String'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
