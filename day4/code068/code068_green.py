def solution(arr, k):
    if k % 2 == 0:
        return list(i + k for i in arr)
    else:
        return list(i * k for i in arr)
