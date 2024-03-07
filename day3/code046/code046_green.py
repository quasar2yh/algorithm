def solution(num_list):
    count = 1
    if len(num_list) > 10:
        for i in num_list:
            count += i
        count -= 1
    else:
        for i in num_list:
            count *= i
    return count

