def solution(array, n):
    answer = len([1 for arr in array if arr==n])
    return answer