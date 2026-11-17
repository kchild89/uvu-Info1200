import functools

numlist = [1, 2, 3, 4, 5, 6]

def add_square(total, current):
    return total + (current * current)

total = functools.reduce(add_square, numlist)

print(total)