import math
# 피자 나눠 먹기 (3)


def solution(slice, n):
    return 1 if slice >= n else math.ceil(n/slice)