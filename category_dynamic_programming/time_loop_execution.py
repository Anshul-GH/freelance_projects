import timeit

# setup_code = "from math import factorial"
setup_code = "import random"

statement = """
# convert days to index
# query_idx = [random.randint(1,1000000000) for i in range(100000)]
# stockData = [random.randint(1,1000000000) for i in range(100000)]

query_idx = [i for i in range(100000000)] #range(99999999, 0, -1)
stockData = [i for i in range(100000000)]

# output_day_set
out_day = []

for day in query_idx:
    min_price = stockData[day]
    day_found = False
    
    for i in range(1, max(day,len(stockData)-day)):
        prev = day-i
        nxt = day+i
        if prev >= 0 and stockData[prev] < min_price:
            out_day.append(prev+1)                        
            day_found = True
            break
        if nxt < len(stockData) and stockData[nxt] < min_price:
            out_day.append(nxt+1)                        
            day_found = True
            break
    
    if not day_found:
        out_day.append(-1)
"""

print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 1)}")