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
    days_max = max(days_set)
    days_min = min(days_set)

    days_list = list(range(days_min, days_max+1))
    print(days_list)
    print(days_set)


    
    # count of possible meetings
    mtng_cnt = 0
        
    # assuming all the investors have a defines firstDay and lastDay
    # that is, len(firstDay) = len(lastDay)

    for i in range(len(firstDay)):
        if len(days_list) > 0:
            days_max = max(days_list)
            days_min = min(days_list)
            
            if firstDay[i] >= days_min:
                if firstDay[i] in days_list:
                    days_list.remove(firstDay[i])
                    mtng_cnt += 1    
            elif lastDay[i] <= days_max:
                if lastDay[i] in days_list:
                    days_list.remove(lastDay[i])
                    mtng_cnt += 1
    
    # return the consolidated meeting count
    return mtng_cnt
            # break            



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
