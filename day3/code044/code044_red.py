'''
이어 붙인 수
제출 내역
문제 설명
정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list):
    answer = 0
    odd_str = ''
    even_str = ''
    for i in num_list:
        if i%2 == 0:
            even_str += str(i)
        else:
            odd_str += str(i)
    answer = int(even_str) + int(odd_str)
    return answer