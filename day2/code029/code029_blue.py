def solution(s1, s2):
    answer = 0
    for string_1 in s1:
        for string_2 in s2:
            if string_1 == string_2:
                answer += 1    
    return answer