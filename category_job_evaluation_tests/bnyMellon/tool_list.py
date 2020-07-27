#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'toolchanger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY tools
#  2. INTEGER k
#  3. STRING q
#

def toolchanger(tools, k, q):
    # find all the absolute distance of all the indexes of query value(q) from the current position 
    idx_q = [min(abs(idx-k), abs(len(tools) - idx + k)) for idx, val in enumerate(tools) if val == q]
    
    # return the min of the distances as answer
    return min(idx_q)
    




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tools_count = int(input().strip())

    tools = []

    for _ in range(tools_count):
        tools_item = input()
        tools.append(tools_item)

    k = int(input().strip())

    q = input()

    result = toolchanger(tools, k, q)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
