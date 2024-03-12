def solution(my_string):
    answer = ''
    for s in my_string:
        answer+=s.lower() if ord(s)<=90 else s.upper()
    return answer