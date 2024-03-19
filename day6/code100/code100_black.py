# 주사위 게임 1

"""
1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때
얻는 점수는 다음과 같습니다.

a와 b가 모두 홀수라면 a^2 + b^2 점을 얻습니다.
a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.
두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

"""


def solution(a, b):
    """
    연산이 복잡해질 경우를 고려
    if elif 마다 계속 연산하는 거 방지
    """
    calc_judge = []
    calc_judge.append(True) if a % 2 == 0 else calc_judge.append(False)
    calc_judge.append(True) if b % 2 == 0 else calc_judge.append(False)
    if all(calc_judge):
        return abs(a - b)
    elif any(calc_judge):
        return 2 * (a + b)
    else:
        return a**2 + b**2


print(solution(6, 1))
