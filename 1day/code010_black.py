def solution(n):
    if n <= 0 or n > 1000:
        return "숫자는 0초과 1000이하의 숫자만 입력 가능합니다."
    li = [i for i in range(2, n+1) if i % 2 == 0]
    answer = sum(li)
    return answer


print(solution(4))
