# Fibonacci code with recursion

# function to print nth Fibonacci number
def Fibonacci(n):
    if n == 1 or n == 2:
        return (n-1)
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

# main
if __name__ == "__main__":
    n = int(input("Enter the range: "))
    if n <= 0:
        print("Please enter a positive integer")
    else:
        for i in range(1,n+1):
            print(Fibonacci(i))