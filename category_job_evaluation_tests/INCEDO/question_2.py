'''
2. Given a string, find the length of the longest substring without repeating characters.

Input: 90
Output: 5
Input: 84
Output: 7
'''

import math

def find_largest_pf(num):
    pf_list = []

    if num % 2 == 0:
        pf_list.append(2)
    
    # get the square root of the number
    sqrt_num = int(math.sqrt(num))

    # choose all the odd numbers starting from 3 as potential prime factors (pf)
    for i in range(3, sqrt_num, 2):
        while num % i == 0:
            pf_list.append(i)
            num = num / i
    
    # remove duplicates
    pf_list = list(set(pf_list))

    # sort the list to push the largest pf to end
    pf_list.sort()

    print("Largest Prime Factor: ", pf_list[-1])



if __name__ == "__main__":
    print("Enter the number:")
    num = int(input())
    find_largest_pf(num)
