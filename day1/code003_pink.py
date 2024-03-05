#숫자 비교하기
def solution(num1, num2):
    answer = 0
    if num1 == num2 :
        return 1
    else:
        return -1
    return answer
# 예  a == b 일때 , == 는 a와 b를 비교하여 같으면 True 다르면 false라는 불리언타입을 반환합니다.
# 따라서 본 문제에서 조건문을 만들때 num1 == num2를 하면 둘을 비교해서 true면 1 을 반환하고 그렇지 않으면 -1을 반환하도록 코드를 짜 보았습니다. 