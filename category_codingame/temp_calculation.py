import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
if n == 0:
    print(0)
else:
    temps = input().split()
    temps = [int(val) for val in temps]
    temps.sort()
    max_t = -274

    if n == 1:
        max_t = temps[0]
    else:
        for val in temps:
            if (val >= 0 and max_t > val) | \
            (val <= 0 and max_t < val) | \
            (val > 0 and max_t <= -val) | \
            (val < 0 and max_t > -val):
                max_t = val

    print(max_t)