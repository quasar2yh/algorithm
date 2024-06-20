"""
n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, 
arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]
"""


def solution(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


# 우수 답변
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))

