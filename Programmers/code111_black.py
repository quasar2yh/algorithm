# 최댓값 만들기 (2)

"""
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 
solution 함수를 완성해주세요.
"""

def solution(numbers):
    numbers = sorted(numbers)
    max_candidate1 = numbers[-1] * numbers[-2]
    max_candidate2 = numbers[0] * numbers[1]
    return max(max_candidate1, max_candidate2)
