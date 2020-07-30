# import itertools

# lst = [0,1,2,3,4,5,6,7,8,9,-1]

# day = 11

# for i in range(day-1, 0, -1):
#     print(lst[i-1])




# # day = 10
# # day_found = False

# # for i in range(1, len(lst) - day - 1):
# #     prev = 10
# #     nxt = 10
# #     if (day - i) >= 0:
# #         prev = day - i
# #         day_found = True        
# #     else:
# #         day_found = False
# #     if not day_found and day + i < len(lst):
# #         nxt = day + i
# #         day_found = True
    
# #     print(day_found, lst[prev], lst[nxt])



# # #!/bin/python3

# # import math
# # import os
# # import random
# # import re
# # import sys

# # #
# # # Complete the 'predictAnswer' function below.
# # #
# # # The function is expected to return an INTEGER_ARRAY.
# # # The function accepts following parameters:
# # #  1. INTEGER_ARRAY stockData
# # #  2. INTEGER_ARRAY queries
# # #

# # def predictAnswer(stockData, queries):
# #     # print(stockData)
# #     # print(queries)
# #     # print(q_idx)

# #     # convert days to index
# #     # query_idx = [val -1 for val in queries]

# #     # # merge price and index together for stockData
# #     # stock_list = []
# #     # for i in range(len(stockData)):
# #     #     stock_list.append([stockData[i], i])
    
# #     # # sort based on stock price
# #     # stock_list.sort()
    
# #     # # variable to hold minimum stock price identified
# #     # min_price = 0

# #     # for day in query_idx:
# #     #     if day == 0:
# #     #         if 

# #     #     for data in stock_list:
# #     #         if day == 0:

# #     #         if data[1] == day and day > 0:




# #     # convert days to index
# #     query_idx = [val-1 for val in queries]
# #     # print(query_idx)

# #     # output_day_set
# #     out_day = []

# #     for day in query_idx:
# #         # print()
# #         # print(day)
# #         min_price = stockData[day]
# #         # print(min_price)
# #         day_found = False
# #         if day > 0:
# #             # if day >= int(len(stockData) / 2):
# #             for i in range(day, len(stockData)-1):
# #                 prev = i-1 #len(stockData)-1-i
# #                 nxt = i+1
# #                 if (prev) >= 0:
# #                     if stockData[prev] < min_price:
# #                         min_price = stockData[prev]
# #                         out_day.append(prev+1)
# #                         # print(min_price, out_day)
# #                         day_found = True
# #                         break
# #                     elif stockData[nxt] < min_price:
# #                         min_price = stockData[nxt]
# #                         out_day.append(nxt+1)
# #                         # print(min_price, out_day)
# #                         day_found = True
# #                         break
# #         elif day == 0:
# #             for i in range(day, len(stockData)-1):
# #                 nxt = i+1
# #                 if stockData[nxt] < min_price:
# #                     min_price = stockData[nxt]
# #                     out_day.append(nxt+1)
# #                     # print(min_price, out_day)
# #                     day_found = True
# #                     break

        
# #         if not day_found:
# #             out_day.append(-1)
    
# #     return out_day

            
        




# # if __name__ == '__main__':
# #     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

# #     stockData_count = int(input().strip())

# #     stockData = []

# #     for _ in range(stockData_count):
# #         stockData_item = int(input().strip())
# #         stockData.append(stockData_item)

# #     queries_count = int(input().strip())

# #     queries = []

# #     for _ in range(queries_count):
# #         queries_item = int(input().strip())
# #         queries.append(queries_item)

# #     result = predictAnswer(stockData, queries)

# #     print(result)

# #     # fptr.write('\n'.join(map(str, result)))
# #     # fptr.write('\n')

# #     # fptr.close()



data = [5,3,4,6,5,4,6,8,9,5,7]
dictn = {}

for idx, val in enumerate(data):
    dictn[idx] = val

print(dictn)

test = 9

# idxs = []

# val = dictn[test]
# print(val)

# print(dictn.values())

# idxs = dictn[dictn.values() == val]

# print(idxs)

keys = list(dictn.keys())
values = list(dictn.values())

print(keys, values)

flag = values[keys.index(9)] in values
print(flag)
