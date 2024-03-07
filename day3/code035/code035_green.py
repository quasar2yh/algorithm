def solution(n):
    result = []
    for i in range(n + 1):
        for j in range(n + 1):
            if i * j == n:
                result.append((i, j))
    return len(result)
