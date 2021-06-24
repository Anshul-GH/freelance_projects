# conventional function
def square(num):
    return num * num

# lambda function
square_lambda = lambda num: num * num
# square_lambda = lambda num: num * num * 2 # To test assertion failure, use this

try:
    assert square(4) == square_lambda(4)
    print('True')
except:
    print('False')
