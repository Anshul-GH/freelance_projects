# I will be using tkinter as the client wanted a minimalistic ui to chose the source input file
import tkinter as tk
from tkinter import filedialog
from config import get_config

def chose_input():
    # define the root directory
    root = tk.Tk()
    # hide the intrusive root window using withdraw
    root.withdraw()

    # display the minimalistic file open dialog for the user to chose the input text file
    inp_file = filedialog.askopenfilename()
    inp_file = open(file=inp_file)

    source_data = inp_file.read()

    return source_data


def process_substrings(data):
    # read the min_k and max_k values from the config file
    min_k = get_config("MIN_K", default=2)
    max_k = get_config("MAX_K", default=6)

    # placehoders for the substring with the max frequency and corresponding length
    max_freq = 0
    max_str = ''

    # validate that min_k and max_k values are logically correct
    if min_k < max_k and max_k < len(data):
        # starting with the largest (length: max_k) possible substring
        # and moving to the smallest (length: min_k)
        for length in range(max_k, min_k-1, -1):
            # find the frequency for each chosen substrings of specific length
            substr, frequency = find_frequency(data, length)

            # we repeat the comparison again to find the max frequency string across all lengths
            if frequency > max_freq:
                max_str = substr
                max_freq = frequency

    # return the maximum frequency string data
    return max_str, max_freq


def find_frequency(data, length):
    # placehoders for the substrings with the max frequency for a specific length = length
    max_freq = 0
    max_str = ''

    # the maximum possible iterations for the substrings of the specific length = length
    iterations = len(data) - length

    # iterate through each substring
    for index in range(iterations):
        # frequency counter
        frequency = 0
        # choose the substring
        substr = data[index:length+index]
        
        # for the chosen substring, look for match and increment the frequency
        for subindex in range(iterations):
            if data[subindex:length+subindex] == substr:
                frequency += 1

        # store the string with maximum frequency and the corresponding length
        if frequency > max_freq:
            max_str = substr
            max_freq = frequency
    
    return max_str, max_freq


if __name__ == '__main__':
    # open the file dialog for the user to chose input
    source_data = chose_input()

    # create another function to iteratively process each possible substring
    substr, frequency = process_substrings(source_data)

    # print the output on the console
    print(substr, frequency)


