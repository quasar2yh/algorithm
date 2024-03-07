'''
문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_string):
    answer = sum([int(s) for s in my_string if s in '123456789'])
    return answer