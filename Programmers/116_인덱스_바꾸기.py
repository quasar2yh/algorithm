"""
https://school.programmers.co.kr/learn/courses/30/lessons/120895?language=python3
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 
return 하도록 solution 함수를 완성해보세요.
"""


def solution(my_string, num1, num2):
    chr1, chr2 = my_string[num1], my_string[num2]
    my_string = my_string[:num1] + chr2 + \
        my_string[num1+1:num2] + chr1 + my_string[num2+1:]
    return my_string


print(solution("I love you", 3, 6))

# 리스트로 형변환 후 바꾸고 join 할 수 도 있음
