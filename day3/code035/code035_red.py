'''
순서쌍의 개수
제출 내역
문제 설명
순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요
'''
def solution(n):
    answer = 1
    i = 2
    power_numbers = []
    p = 0
    while i <= n:
        if n%i == 0:
            n = n/i
            p += 1
        else:
            i += 1
            if p != 0:
                power_numbers.append(p)
                p = 0
    power_numbers.append(p)
    for i in power_numbers:
        answer = answer*(i+1)
    return answer