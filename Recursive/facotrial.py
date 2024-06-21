import time


def iter_factorial(num):
    total = 1
    while num:
        if num != 1:
            total = total * num
        num -= 1
    return total


def recursive_factorial(num):
    if num == 1:
        return 1
    return num * recursive_factorial(num-1)


