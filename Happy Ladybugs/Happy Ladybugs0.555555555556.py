#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    bugs=set(b)
    if '_' in bugs:
        for i in bugs:
            if b.count(i)>1 or i=='_':
                pass
            else: return 'NO'
        return 'YES'
    else:
        for i in range(1,len(b)-1):
            if b[i]==b[i-1] or b[i]==b[i+1]: pass
            else: return 'NO'
        return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
