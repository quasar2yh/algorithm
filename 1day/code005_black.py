def solution(num1, num2):
    if num1 < 0 or num1 > 100:
        return "첫번째 인자는 0에서 100사이 수를 입력해주세요"
    if num2 < 0 or num2 > 100:
        return "두번째 인자는 0에서 100사이 수를 입력해주세요"
    return num1//num2
