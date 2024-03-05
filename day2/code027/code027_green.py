def solution(num_list):
    a = sum(1 for i in num_list if i % 2 == 0)
    b = sum(1 for i in num_list if i % 2 != 0)
    return [a,b]
