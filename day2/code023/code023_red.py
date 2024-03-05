import math
def solution(n):
    answer = n//7+math.ceil(n/7-n//7)
    return answer