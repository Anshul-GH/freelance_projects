#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY rounds
#

import numpy as np

def maxValue(n, rounds):
    portfolio = [0] * n    

    for rnd in rounds:
        for i in range(rnd[0]-1, rnd[1]):
            portfolio[i] = portfolio[i] + rnd[2]            
    
    max_amt = max(portfolio) 

    # ########################

    # portfolio = [0] * n    

    # for rnd in rounds:
    #     pf_copy = [0] * n
    #     print(pf_copy)
    #     rng = rnd[1] - rnd[0] + 1
    #     pf_copy[rnd[0]-1:rng+1] = [rnd[2]]*(rng)
    #     print(pf_copy)
    #     print(portfolio)
    #     portfolio = list(np.array(portfolio) + np.array(pf_copy))
    #     # [sum(x) for x in zip(portfolio, pf_copy)]
          
    
    # max_amt = max(portfolio)

    return max_amt





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    rounds_rows = int(input().strip())
    rounds_columns = int(input().strip())

    rounds = []

    for _ in range(rounds_rows):
        rounds.append(list(map(int, input().rstrip().split())))

    result = maxValue(n, rounds)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
