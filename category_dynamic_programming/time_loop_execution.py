import timeit

setup_code = "from math import factorial"

statement = """
firstDay = [i for i in range(100000)]
lastDay = [i+1 for i in range(100000)]

# set containing all unique days possible
days_set = set(firstDay + lastDay)
days_full_set = set(list(range(max(days_set), min(days_set)-1, -1)))

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
"""

print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 1)}")