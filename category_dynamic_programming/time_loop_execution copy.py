import timeit

# setup_code = "from math import factorial"
# setup_code = "import random"
setup_code = "from random import randint"

statement = """
stockData = [randint(1, 1000000000) for val in range(100000)]
queries = [randint(1, 100000) for val in range(100000)]



def predictAnswer(stockData, queries):
    # convert days to index
    query_idx = [val - 1 for val in queries]

    # output_day_set
    out_day = []

    for day in query_idx:
        min_price = stockData[day]

        prev = day - 1
        nxt = day + 1

        leftIdx = -1
        while prev > 0:
            if stockData[prev] < min_price:
                leftIdx = prev
                break
            prev -= 1


        rightIdx = -1
        while nxt < len(stockData):
            if stockData[nxt] < min_price:
                rightIdx = nxt
                break
            nxt += 1

        if leftIdx == -1 and rightIdx == -1:
            out_day.append(-1)  # Not found either side
        elif leftIdx == -1:
            out_day.append(rightIdx + 1)
        elif rightIdx == -1:
            out_day.append(leftIdx + 1)
        else:
            if rightIdx - day < day - leftIdx:
                out_day.append(rightIdx + 1)
            else:
                out_day.append(leftIdx + 1)

    return out_day

print(predictAnswer(stockData, queries))
"""

print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 1)}")