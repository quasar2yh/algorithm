# 조건에 맞게 수열 변환하기 1
"""
정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 
50보다 작은 홀수라면 2를 곱합니다. 
그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.
"""

def solution(arr):
    new_li = []
    for num in arr:
        if num>=50 and num%2==0:
            new_li.append(num/2)
        elif num<50 and num%2!=0:
            new_li.append(num*2)
        else:
            new_li.append(num)
    return new_li