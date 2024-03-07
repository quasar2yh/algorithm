# 이어 붙인 수
"""
정수가 담긴 리스트 num_list가 주어집니다. 
num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

입출력 예 #1
    홀수만 이어 붙인 수는 351이고 짝수만 이어 붙인 수는 42입니다. 두 수의 합은 393입니다.
"""

def solution(num_list):
    even, odd = "", ""
    for num in num_list:
        if num%2 == 0:
            even += str(num)
        else:
            odd += str(num)
    return int(even) + int(odd)
