# 제곱수 판별하기
"""
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
"""
import math


def solution(n):
    sqrt = math.sqrt(n)
    return 1 if int(sqrt) == sqrt else 2


# 우수 풀이:
# 루트는 0.5승이야 바보야
# float 데이터 타입이라도 소수점 자리가 0이면 is_integer() 함수는 True를 반환함
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
