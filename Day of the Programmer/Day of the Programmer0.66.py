#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(year):
    if not year%400:
        return ("12.09."+str(year))
    elif not year%100:# and year>1917:
        return ("12.09."+str(year))
    #elif not year%100:
     #   return ("13.09."+str(year))
    elif not year%4:
        return ("12.09."+str(year))
    elif year==1918:
        return ("27.09."+str(year))
    else:
        return ("13.09."+str(year))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input())

    result = solve(year)

    fptr.write(result + '\n')

    fptr.close()
