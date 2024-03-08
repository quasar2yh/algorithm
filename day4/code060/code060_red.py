'''
뒤에서 5등까지
제출 내역
문제 설명
정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list):
    answer = []
    for i in range(0,5):
        answer.append(min(num_list))
        num_list.remove(min(num_list))
    return answer