'''
가위 바위 보
제출 내역
문제 설명
가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
'''

def solution(rsp):
    answer = ''
    rsp_dic = {'2':'0','0':'5','5':'2'}
    for i in rsp:
        answer += rsp_dic[i]
    return answer