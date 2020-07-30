#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'predictAnswer' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockData
#  2. INTEGER_ARRAY queries
#

def find_idx(lst, lnth, price): 
    idx = -1
    counter = 0
    while(counter < lnth):
        if (lst[counter] < price): 
            if (counter < lnth): 
                idx = counter
                break

        counter += 1
    return(idx)

def predictAnswer(stockData, queries):
    # convert days to index
    query_idx = [val-1 for val in queries]

    # output_day_set
    out_day = []

    for day in query_idx:
        l1 = stockData[:day][::-1]
        l2 = stockData[day+1:]

        prev_idx = find_idx(l1, len(l1), stockData[day])
        nxt_idx = find_idx(l2, len(l2), stockData[day])

        if prev_idx <= nxt_idx and prev_idx != -1:
            out_day.append(day-prev_idx)
        elif prev_idx > nxt_idx and nxt_idx != -1:
            out_day.append(day+nxt_idx+2)
        elif prev_idx == -1 and nxt_idx == -1:
            out_day.append(-1)
        elif prev_idx == -1:
            out_day.append(day+nxt_idx+2)
    
    return out_day




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockData_count = int(input().strip())

    stockData = []

    for _ in range(stockData_count):
        stockData_item = int(input().strip())
        stockData.append(stockData_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = predictAnswer(stockData, queries)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()