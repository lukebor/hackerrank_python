#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    #Check the common part of strings
    common_length=0
    for i in range(min(len(s),len(t))):
        if t[i]==s[i]:
            common_length+=1
        else: break
    #count moves to achieve common part (abs(len string1 - string2)) = k1
    k1=max(len(s),len(t))-common_length
    #if common part lenght*2 =k-k1 then yes
    if common_length*2<=k-k1: return 'Yes'
    #else if k-k1 is even then yes
    elif (k-k1)%2==0: return 'Yes'
    #else no
    else: return 'No'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
