'''
flag에 따라 다른 값 반환하기
제출 내역
문제 설명
두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.
'''
def solution(a, b, flag):
    answer = a+b if bool(flag) else a-b
    return answer