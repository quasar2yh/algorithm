def solution(num_list):
    reverse_li = []
    for i in range(len(num_list)):
        end_num = num_list.pop()
        reverse_li.append(end_num)
    return reverse_li


print(solution([1, 0, 1, 1, 1, 3, 5]))
