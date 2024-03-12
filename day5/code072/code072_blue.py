def solution(myString, pat):
    p = myString.lower().find(pat.lower())
    answer = 1 if p >= 0 else 0
    return answer