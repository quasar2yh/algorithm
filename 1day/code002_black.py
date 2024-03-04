def solution(num1, num2):
    if num1 < 0 or num1 > 100:
        return "num1에는 0에서 100사이 숫자만 입력해주세요"
    if num2 < 0 or num2 > 100:
        return "num2에는 0에서 100사이 숫자만 입력해주세요"
    return num1*num2


print(solution(3, 4))
