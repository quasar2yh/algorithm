'''
공배수
제출 내역
문제 설명
정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.
'''
def solution(number, n, m):
    answer = 0
    if number%n == 0 and number%m == 0:
        answer = 1
    return answer