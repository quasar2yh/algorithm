def solution(dot):
    table = [[2,1], 
             [3,4]]
    answer = table[0 if dot[1]>0 else 1][1 if dot[0]>0 else 0]
    return answer