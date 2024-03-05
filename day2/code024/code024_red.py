def solution(numbers):
    number1 = max(numbers)
    numbers.remove(number1)
    number2 = max(numbers)
    answer = number1 * number2
    return answer