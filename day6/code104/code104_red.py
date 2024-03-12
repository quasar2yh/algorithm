'''
x 사이의 개수
제출 내역
문제 설명
문자열 myString이 주어집니다. myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
'''


def solution(myString):
    answer = []
    count = 0
    for i in myString:
        if i == 'x':
            answer.append(count)
            count = 0
        else:
            count += 1
    answer.append(count)
    return answer
