# map function
domain = [1,2,3,4,5]
# f(x) = x * 2
range = map(lambda num: num * 2, domain)
print(list(range))


# filter function
evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))


# reduce function
from functools import reduce
the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)


# sorted function
words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']

print('Sorting by default: ')
print(sorted(words)) 

print('Sorting with lambda key: ')
print(sorted(words, key=lambda s: s.lower()))

print("Sorting with 'sort' method: ")
words.sort(key=str.lower, reverse=False)
print(words)