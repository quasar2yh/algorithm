'''
짝수는 싫어요
제출 내역
문제 설명
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(n):
    answer = []
    i = 0
    while 2*i+1 <= n:
        answer.append(2*i+1)
        i += 1
    return answer
