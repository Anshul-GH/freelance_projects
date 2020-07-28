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

def countMeetings(firstDay, lastDay):
    # set containing all unique days possible
    days_set = set(firstDay + lastDay)
    print(days_set)
    days_list = list(range(min(days_set), max(days_set)+1))
    print(days_list)
    
    # count of possible meetings
    mtng_cnt = 0
        
    # assuming all the investors have a defines firstDay and lastDay
    # that is, len(firstDay) = len(lastDay)
    for i in range(len(firstDay)):
        
        # if the set is empty, break out of the loop
        if not bool(days_set):
            break
        
        for val in range(firstDay[i], lastDay[i] + 1):
            if val in days_list:
                days_list.remove(val)
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

    firstDay_count = int(input().strip())

    firstDay = []

    for _ in range(firstDay_count):
        firstDay_item = int(input().strip())
        firstDay.append(firstDay_item)

    lastDay_count = int(input().strip())

    lastDay = []

    for _ in range(lastDay_count):
        lastDay_item = int(input().strip())
        lastDay.append(lastDay_item)

    result = countMeetings(firstDay, lastDay)

    print("MeetingCount: ", result)

    # fptr.write(str(result) + '\n')

    # fptr.close()