'''
문자열 정수의 합
제출 내역
문제 설명
한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer