def solution(n):
    n > 0 and n <= 1000
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer
