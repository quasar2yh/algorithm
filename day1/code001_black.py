def solution(num1, num2):
    if num1 < -5000 or num1 > 5000:
        return "-5000이상 5000이하의 수를 입력해주세요."
    if num2 < -5000 or num2 > 5000:
        return "-5000이상 5000이하의 수를 입력해주세요."
    return num1-num2
