#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minNum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER samDaily
#  2. INTEGER kellyDaily
#  3. INTEGER difference
#

def minNum(samDaily, kellyDaily, difference):
    day_count = 0
    tot_kelly = 0
    tot_sam = 0

    # scenario where kelly cannot surpass sam
    # 1. kelly solves less problems daily than sam
    # # 2. sam is already behind kelly even after the headstart(difference)
    if (kellyDaily <= samDaily): # or (samDaily + difference < kellyDaily)
        day_count = -1
    # day1
    elif day_count == 0:
        tot_sam = samDaily + difference
        tot_kelly = kellyDaily
        # kellyDaily += kellyDaily
        day_count += 1

    while tot_sam >= tot_kelly:
        tot_kelly += kellyDaily
        tot_sam += samDaily        
        day_count += 1

    return day_count




    while kellyDaily < samDaily:
        kellyDaily += kellyDaily


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    samDaily = int(input().strip())

    kellyDaily = int(input().strip())

    difference = int(input().strip())

    result = minNum(samDaily, kellyDaily, difference)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
