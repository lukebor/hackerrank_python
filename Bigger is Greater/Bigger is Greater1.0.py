#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    buf='{'
    j=0
    chars = [i for i in w]
    x=len(chars)-1
    while x>0 and chars[x-1]>=chars[x]:
        x-=1
    if not x: return -1
    swap=chars[x-1]
    for i in range(x,len(chars)):
        if chars[i]>swap and (ord(chars[i])-ord(swap))<ord(buf):
            buf=chr(ord(chars[i])-ord(swap))
            j=i
    chars[x-1]=chars[j]
    chars[j]=swap
    chars[x:]=sorted(chars[x:])
    if ''.join(i for i in chars)==w: return 'no answer'
    else: return ''.join(i for i in chars)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
        if result==-1: result='no answer'
        fptr.write(result + '\n')

    fptr.close()
