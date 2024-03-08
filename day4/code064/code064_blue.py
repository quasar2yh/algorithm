'''
홀짝에 따라 다른 값 반환하기
제출 내역
문제 설명
양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(n):
    answer = 0
    for i in range(n,0,-2):
        answer += i**2 if i % 2 == 0 else i
    return answer