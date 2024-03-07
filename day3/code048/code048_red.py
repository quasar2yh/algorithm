'''
원소들의 곱과 합
제출 내역
문제 설명
정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.
'''
from functools import reduce
def solution(num_list):
    answer = 0
    def mult(a,b):
        return a*b
    multiple_num = reduce(mult,num_list) 
    square_num = sum(num_list)**2
    if multiple_num < square_num:
        answer = 1
    return answer