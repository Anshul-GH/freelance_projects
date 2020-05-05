Problem Statement
-----------------

- DNA sequences are represented in form of strings with a combination of only the following letters - a, g, c and t
- Source input for us is a single string of dna sequence (could be of any length - typically in the range of thousands or more).
- We need to identify a substring within the source, with a given minimum (min_k) and maximum (max_k) possible lengths, that is repeating within the sequence at the highest frequency.
- If there is a tie between the frequency of occourance of two substrings, the one which is larget is chosen.
- If they are of the same length, any one can be chosen at random.
- Essentially we are looking for a possible 'viral' sequence that is repeating.

- For Example:
source_input = 'gactctcagc'
min_k = 2
max_k = 6

- This would return 'ctc'(frequency of occourance: 2), 'ct' (frequency: 2), 'tc' (frequency: 2) are the most repeating ones.
- Hence 'ctc' which has the maximum length, must be chosen as the answer.

This was one of my assignments at upwork and I am just showing how I implemented this.
Its no way, the only way. Please share your inputs - happy to be corrected and learn :).

Lets get started !!

Lets make the min_k, max_k values configurable outside the main code file.
Its a fairly simple thing to do and helps avoid changes to the code unnecessarily

Lets test the code with the sample input that we had discussed earlier:
- For Example:
source_input = 'gactctcagc'
min_k = 2
max_k = 6

Output should be 'ctc' and 2

I found the issue ... silly mistake ... I named the method input param using a keyword/reserved 'len'
lets fix it

So its works now :)


Lets test this with another realistic example that clint shared with me.
There is a dna sequence of length 6000+ that has the substring cttt getting repeated 52 times ... lets test the code for that sample

Also for this example, the min_k and max_k values to be used are 4 and 9, as per the client
Lets update the config file

Lets test now


So we got the output we expected.
The code is working !

I will now be working on optimizing this further.
Please share suggestions, if any.
Eager to learn :)

Thanks for watching !!
