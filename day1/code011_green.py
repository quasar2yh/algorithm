def solution(arr):
    answer=0
    for i in arr:
        i=int(i)
        answer += i
    answer = answer/len(arr)
    return answer
