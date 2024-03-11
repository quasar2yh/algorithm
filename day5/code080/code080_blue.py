def solution(my_string, is_prefix):
    answer = 1 if my_string[::-1].find(is_prefix[::-1]) == 0 else 0
    return answer