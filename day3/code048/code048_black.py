# 원소들의 곱과 합
"""
정수가 담긴 리스트 num_list가 주어질 때, 
모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 
return하도록 solution 함수를 완성해주세요.
"""


def solution(num_list):
    sum_answer = eval('('+'+'.join(list(map(str, num_list)))+')**2')
    multi_answer = eval('*'.join(list(map(str, num_list))))
    return 1 if multi_answer < sum_answer else 0


