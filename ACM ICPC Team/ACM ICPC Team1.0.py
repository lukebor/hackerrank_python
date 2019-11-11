#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    x=0
    res=0
    result=0
    for i in range(n):
        for j in range(i,n):
            x=int(topic[i],2) | int(topic[j],2)
            if str(bin(x)).count('1')==res: result+=1
            if str(bin(x)).count('1')>res: result=1
            res=max(str(bin(x)).count('1'),res)
            x=0
    return [res,result]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
