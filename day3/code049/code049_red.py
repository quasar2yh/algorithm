'''
문자열 곱하기
제출 내역
문제 설명
문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(my_string, k):
    answer = ''
    for i in range(k):
        answer += my_string
    return answer