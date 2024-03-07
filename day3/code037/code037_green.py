def solution(my_string):
    list = ['a','e','i','o','u']
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] not in list:
            answer += my_string[i]
    return answer
