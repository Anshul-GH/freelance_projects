# Fibonacci code without recursion
n = int(input("Enter the range:"))

# initializing the first two numbers
n1 = 0
n2 = 1
counter = 0

if n <= 0:
    print('Please enter a positive integer.')
elif n == 1:
    print(f"Fibonacci Sequence upto range {n}:")
    print(n1)
else:
    print(f"Fibonacci Sequence upto range {n}:")
    while counter < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        counter += 1
