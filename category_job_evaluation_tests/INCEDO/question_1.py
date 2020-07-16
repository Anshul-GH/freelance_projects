'''
1. Find four elements a, b, c and d in an array such that a+b = c+d

Input:   {3, 4, 7, 1, 2, 9, 8}
Output:  (3, 8) and (4, 7)
Explanation: 3+8 = 4+7

Input:  {65, 30, 7, 90, 1, 9, 8};
Output:  No pairs found
'''

def detect_pairs(arr_len, arr):
    # sort the array
    arr.sort()

    print("Output:")
    arr_pair_sums = {}
    no_pairs = True
    for i in range(arr_len - 1):
        for j in range(i+1, arr_len):
            pair_sum = arr[i] + arr[j]
            # check if similar sum was previously recorded
            # if yes, pubilsh as a match
            if pair_sum in arr_pair_sums.keys():
                print("({},{}) and {}".format(arr[i], arr[j], arr_pair_sums[pair_sum]))
                arr_pair_sums[pair_sum] = str(arr_pair_sums[pair_sum] + ",(" + str(arr[i]) + "," + str(arr[j]) + ")")
                no_pairs = False
            else:
                # if its a new sum, add it to the dict that holds pairs with same sum together
                arr_pair_sums[pair_sum] = "(" + str(arr[i]) + "," + str(arr[j]) + ")"
    
    # if no pairs are found - print No pairs found
    if no_pairs:
        print("No pairs found")


if __name__ == "__main__":
    print("Enter the count of numbers:")
    arr_len = int(input())
    arr = []
    print("Enter the {} numbers.".format(arr_len))
    print("(Please press return(enter) key after each number entered.):")
    for i in range(arr_len):
        arr.append(int(input()))

    detect_pairs(arr_len, arr)
