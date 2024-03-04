def solution(num1, num2):
    if num1 < -50000 or num1 > 50000:
        return "첫번째 인자는 -50000에서 50000사이 수를 입력해주세요"
    if num2 < -50000 or num2 > 50000:
        return "두번째 인자는 -50000에서 50000사이 수를 입력해주세요"
    return num1+num2
