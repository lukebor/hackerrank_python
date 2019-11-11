#!/bin/python3

import sys
import math
def lowestTriangle(base, area):
    return int(math.floor(2*area/base-0.001)+1)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)