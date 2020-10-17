arr = [1,2,3,4,6,7,8,9,12,4,2,5,7,2,5,2,1,4,6,3]
# arr = [21,31,43,57,97,89,63,61,51,75,2,4,6,8,0,12,22,24,12,68,62]
print(arr)
lst = list(sorted(arr, key=lambda x: [x % 2, x]))
print(lst)

# f_idx = 0
# b_idx = len(arr) - 1

# while f_idx < b_idx:
#     if arr[f_idx] % 2 != 0:
#         if arr[b_idx] % 2 != 0:
#             b_idx -= 1
#         else:
#             tmp = arr[f_idx]
#             arr[f_idx] = arr[b_idx]
#             arr[b_idx] = tmp
#     else:
#         f_idx += 1

# print(arr)

# lst = list(sorted(arr, key=lambda x: [x % 2, x]))
# print(lst)