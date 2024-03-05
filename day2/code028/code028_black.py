# 자릿수 더하기
"""
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
"""


def solution(n):
    answer = 0
    for string in str(n):
        answer += int(string)
    return answer

# map 함수 활용 답안


def solution(n):
    answer = sum(list(map(int, list(str(n)))))
    return answer
