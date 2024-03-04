def solution(angle):
    if angle <= 0 or angle > 180:
        return "angle은 0초과 180이하의 숫자만 입력 가능합니다."
    if angle > 0 and angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle > 90 and angle < 180:
        return 3
    elif angle == 180:
        return 4


print(solution(80))
