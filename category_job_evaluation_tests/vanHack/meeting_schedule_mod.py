#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY firstDay
#  2. INTEGER_ARRAY lastDay
#

def countMeetings():
    
    # Execution time is: 364.81144413700076
    # firstDay = [1 for i in range(100000)]
    # lastDay = [9999 for i in range(100000)]

    firstDay = [i for i in range(100000)]
    lastDay = [i+1 for i in range(100000)]
    
    # set containing all unique days possible
    # days_set = set(firstDay + lastDay)
    days_full_set = set(list(range(max(lastDay), min(firstDay)-1, -1)))
    
    # count of possible meetings
    mtng_cnt = 0
        
    # assuming all the investors have a defines firstDay and lastDay
    # that is, len(firstDay) = len(lastDay)
    for i in range(len(firstDay)):
        
        # if the set is empty, break out of the loop
        if not bool(days_full_set):
            break
        
        for val in range(firstDay[i], lastDay[i] + 1):
            if val in days_full_set:
                days_full_set.remove(val)
                mtng_cnt += 1
                break

        # if firstDay[i] in days_set:
        #     days_set.remove(firstDay[i])
        #     mtng_cnt += 1
        # elif lastDay[i] in days_set:
        #     days_set.remove(lastDay[i])
        #     mtng_cnt += 1
    
    # return the consolidated meeting count
    return mtng_cnt

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # firstDay_count = int(input().strip())

    # firstDay = []

    # for _ in range(firstDay_count):
    #     firstDay_item = int(input().strip())
    #     firstDay.append(firstDay_item)

    # lastDay_count = int(input().strip())

    # lastDay = []

    # for _ in range(lastDay_count):
    #     lastDay_item = int(input().strip())
    #     lastDay.append(lastDay_item)

    result = countMeetings()

    print("MeetingCount: ", result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
