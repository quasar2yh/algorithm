from collections import deque


def solution(numbers, direction):
    de_numbers = deque(numbers)
    if direction == "right":
        de_numbers.rotate(1)
    else:
        de_numbers.rotate(-1)
    return list(de_numbers)


print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
