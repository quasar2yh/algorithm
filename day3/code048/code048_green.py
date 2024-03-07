def solution(num_list):
    mult = 1
    for i in num_list:
        mult *= i
    if mult < sum(num_list)**2:
        return 1
    elif mult > sum(num_list)**2:
        return 0
