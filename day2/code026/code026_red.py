import math
def solution(slice, n):
    answer = n//slice + math.ceil(n/slice-n//slice)
    return answer