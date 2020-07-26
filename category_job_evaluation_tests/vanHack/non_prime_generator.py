from math import sqrt

# function to check if a given number is prime
def check_prime(n):
    is_prime = True
    for num in range(2, int(sqrt(n)) + 1):
        if n % num == 0:
            is_prime = False
            break
    return is_prime


def manipulate_generator(generator, n):
    # flag to ensure that manipulate_generator prints only one value per iteration
    printed = False
    
    while not printed:
        if n == 1:
            # printing 1 by default as its the first non-prime
            print(1)
            # update the flag to indicate value being printed and exit the while loop
            printed = True
        else:
            # check for the number to be prime
            is_prime = check_prime(n)
            
            # if its a non-prime number, print it
            if not is_prime:
                print(n)
                # update the flag to indicate value being printed and exit the while loop
                printed = True
            else:
                # if a prime number is encountered, generate the next number
                n = next(generator)


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    # print(n)
    manipulate_generator(g, n)