'''
    3. Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
'''

def find_longest_substr(strg):
    # convert the string to a list
    str_lst = [chr for chr in strg]
    track_lst = []

    for val in str_lst:
        if val in track_lst:
            break
        else:
            track_lst.append(val)
    

    # substr = ''.join(track_lst)
    
    # printing length of the longest substr
    print("Length of longest non-repeating substring: ", len(track_lst))

if __name__ == "__main__":
    print("Enter the string:")
    strg = input()
    find_longest_substr(strg)