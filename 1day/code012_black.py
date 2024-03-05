def solution(array, height):
    count = 0
    for other in array:
        if other > height:
            count += 1
    return count


print(solution([149, 180, 192, 170], 167))
