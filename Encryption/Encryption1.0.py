#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    res=[]
    res2=[]
    result=''
    s+=' '*(math.ceil(len(s)**0.5)**2-len(s))
    for i in range(int(len(s)**0.5)):
        res.append(s[i*int(len(s)**0.5):i*int(len(s)**0.5)+int(len(s)**0.5)])
    for j in range(int(len(s)**0.5)):
        res2.append([i[j] for i in res if i[j]!=' '])
        res2[j]=''.join(res2[j])
    return ' '.join(res2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
