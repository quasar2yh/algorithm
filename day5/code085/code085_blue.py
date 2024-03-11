def solution(arr):
    answer = []
    for a in arr:
        answer+=[a for _ in range(a)]
    return answer