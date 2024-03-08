'''
n의 배수 고르기
제출 내역
문제 설명
정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.
'''
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n == 0:
            answer.append(i)
        else:
            pass
    return answer
# 변수에 리스트를 할당할떄 값만 복사되는게 아니라 아예 같은 취급을 받게된다
# for문을 돌릴때 기준 리스트가 수정되면 건너뛰어지거나 중복해서 반복되는 경우가 생길 수 있다