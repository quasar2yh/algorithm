def solution(num_list):
    even = len([1 for n in num_list if n%2==0])
    answer = [even, len(num_list)-even]
    return answer