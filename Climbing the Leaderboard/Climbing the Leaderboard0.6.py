#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores_wodup=[]
    rank=[]
    for i in scores:
        if i not in scores_wodup: scores_wodup.append(i)
    for i in alice:
        a=scores_wodup
        a.append(i)
        a=sorted(a,reverse=True)
        rank.append(a.index(i)+1)
    return rank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
