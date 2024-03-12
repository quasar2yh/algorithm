'''
가장 큰 수 찾기
제출 내역
문제 설명
정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(array):
    answer = []
    max_num = 0
    index = 0
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
            index = i
    answer.append(max_num)
    answer.append(index)
    return answer