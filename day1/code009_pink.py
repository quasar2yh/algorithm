# 각도 구하기
def solution(angle):
    answer = 0
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    else:
        return 4
    return answer
# 문제에서 예각은 1 직각은 2 둔각은 3 평각은 4를 출력하라고 하는데 
# 예각 : 0 < angle < 90
# 직각 : angle = 90
# 둔각 : 90 < angle < 180
# 평각 : angle = 180
# 이런 식을 제시해 줍니다.

#  그래서 이 식들을 활용하는 방법으로 코드를 짜 보았고, 직각의 경우는  각도가 90도여야 직각이므로 angle과 90을 비교해서 같게 하기 위해
#  == 으로 바꾸어 주었습니다. 