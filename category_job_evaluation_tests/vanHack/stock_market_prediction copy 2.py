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

def findSmallerValues(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        # the value chosen is the largest value 
        if lys[last] == val:
            return -1
        # the value chosen is the smallest value
        elif lys[first] == val:
            return 0
        mid = (first+last)//2
        if lys[mid]
        if lys[mid] > val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index


def predictAnswer(stockData, queries):
    # convert days to index
    query_idx = [val-1 for val in queries]

    # output_day_set
    out_day = []

    stockDict = {}

    for idx, val in enumerate(stockData):
        if val in stockDict.keys():
            stockDict[val].append(idx)
        else:
            stockDict[val] = [idx]
    
    stockDict_sortedKeys = sorted(stockDict)

    for day in query_idx:
        day_price = stockData[day]


    # for day in query_idx:
    #     min_price = stockData[day]
    #     day_found = False
        
    #     for i in range(1, max(day,len(stockData)-day)):
    #         prev = day-i
    #         nxt = day+i
    #         if prev >= 0 and stockData[prev] < min_price:
    #             out_day.append(prev+1)                        
    #             day_found = True
    #             break
    #         if nxt < len(stockData) and stockData[nxt] < min_price:
    #             out_day.append(nxt+1)                        
    #             day_found = True
    #             break
        
    #     if not day_found:
    #         out_day.append(-1)
    
    # return out_day

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

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

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
