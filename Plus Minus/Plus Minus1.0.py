#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    result=[]
    pos,neg,zero=0,0,0
    for i in range(n):
        if arr[i]>0: pos+=1
        if arr[i]<0: neg+=1 
        if arr[i]==0: zero+=1
    print('{:0.6f}'.format(pos/n),'\n''{:0.6f}'.format(neg/n),'\n''{:0.6f}'.format(zero/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
