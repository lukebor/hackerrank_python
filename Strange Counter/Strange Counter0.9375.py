#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    tier=int(math.log((t/3)+1,2))
    return 3*(2**(tier+1)-1)-t+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
