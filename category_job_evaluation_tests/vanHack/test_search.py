# function to search an element in 
# minimum number of comparisons 
def search(arr, n, price): 
    idx = -1
    counter = 0
    while(counter < n):
        if (arr[counter] < price): 
            if (counter < n): 
                idx = i
                break

        i += 1
    return(idx)

if __name__ == "__main__":
    out_day = []
    arr = [5,6,8,4,9,10,8,3,6,4]
    n = len(arr) 
    days = [3,1,8]

    for day in days:        
        l1 = arr[:day-1][::-1]
        l2 = arr[day:]
        print(l1, l2)
        # print(arr[day-1])
        # prev_idx = day - 1 - search(l1, len(l1), day)
        # nxt_idx = day + 1 + search(l2, len(l2), day)
        prev_idx = search(l1, len(l1), arr[day-1])
        nxt_idx = search(l2, len(l2), arr[day-1])
        print(day, prev_idx, nxt_idx)
        print(day, day-prev_idx-1, day+nxt_idx+1)
        if prev_idx <= nxt_idx and prev_idx != -1:
            out_day.append(day-prev_idx-1)
        elif prev_idx > nxt_idx and nxt_idx != -1:
            out_day.append(day+nxt_idx+1)
        elif prev_idx == -1 and nxt_idx == -1:
            out_day.append(-1)
        elif prev_idx == -1:
            out_day.append(day+nxt_idx+1)
        # else:
        #     print(prev_idx, nxt_idx)

    # print (search(arr, n, x)) 
    # print(prev_idx, nxt_idx)

    print(out_day)