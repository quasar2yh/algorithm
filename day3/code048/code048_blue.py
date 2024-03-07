'''
정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.
'''
def solution(num_list):
    p = 1
    s = sum(num_list)**2
    for n in num_list:
        p*=n
    answer = 1 if p<s else 0
    return answer