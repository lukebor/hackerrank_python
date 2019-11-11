#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    res=[]
    for i in range(n):
        if grades[i]< 38: res.append(grades[i])
        elif grades[i]%5 >2: res.append(grades[i]+5-grades[i]%5)
        else: res.append(grades[i])
        
    return res
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
