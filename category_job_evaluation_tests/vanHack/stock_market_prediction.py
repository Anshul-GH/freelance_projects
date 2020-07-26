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

def predictAnswer(stockData, queries):
    # convert days to index
    query_idx = [val-1 for val in queries]
    
    # output_day_set
    out_day = []

    for day in query_idx:
        min_price = stockData[day]
        day_found = False
        # edge case - last day
        if day == len(stockData)-1:
            for i in range(day-1, 0, -1):
                nxt = i - 1
                if stockData[nxt] < min_price:
                    min_price = stockData[nxt]
                    out_day.append(nxt+1)                    
                    day_found = True
                    break
        # edge case - first day
        elif day == 0:
            for i in range(1, len(stockData)-day):
                nxt = day+i
                if stockData[nxt] < min_price:
                    min_price = stockData[nxt]
                    out_day.append(nxt+1)                    
                    day_found = True
                    break        
        # all the other cases
        elif day > 0:
            for i in range(1, max(day,len(stockData)-day)):
                prev = day-i
                nxt = day+i
                if prev >= 0 and stockData[prev] < min_price:
                    min_price = stockData[prev]
                    out_day.append(prev+1)                        
                    day_found = True
                    break
                if not day_found and nxt < len(stockData) and stockData[nxt] < min_price:
                    min_price = stockData[nxt]
                    out_day.append(nxt+1)                        
                    day_found = True
                    break


        
        if not day_found:
            out_day.append(-1)
    
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
