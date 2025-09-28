#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    # for i in range(n):
    #     while i>0 and arr[i]<arr[i-1]:
    #         arr[i-1],arr[i]=arr[i],arr[i-1]
    #         print(*arr)
    #         i-=1
    key = arr[-1]  # last element to insert
    i = n - 2
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]  # shift right
        print(*arr)          # print after each shift
        i -= 1
    arr[i + 1] = key         # insert key
    print(*arr) 
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
