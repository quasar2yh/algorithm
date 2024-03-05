import math
def solution(slice, n):
    pizza = math.ceil(n/slice)
    if n <= slice:
        return 1
    else:
        return pizza
