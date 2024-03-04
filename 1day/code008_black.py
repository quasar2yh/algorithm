def solution(num1, num2):
    if num1 <= 0 or num1 > 100:
        return "첫번째 인자는 0초과 100이하의 수를 입력해주세요"
    if num2 <= 0 or num2 > 100:
        return "두번째 인자는 0초과 10이하의 수를 입력해주세요"
    return int(num1/num2*1000)


print(solution(1, 16))
