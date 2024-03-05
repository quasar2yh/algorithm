def solution(array, height):
    len(array) >= 1 and len(array) <= 100
    height >= 1 and height <= 200
    count = 0
    for i in array:
        if i >= 1 and i <= 200:
            if i > height:
                count += 1
    return count
