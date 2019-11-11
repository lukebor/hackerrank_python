#!/bin/python3

import sys

def lowestTriangle(base, area):
    return round(2*area/base)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)