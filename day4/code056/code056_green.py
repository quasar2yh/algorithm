def solution(a, b):
    fst = str(a) + str(b)
    snd = 2*a*b
    if int(fst) < snd:
        return snd
    if int(fst) > snd:
        return int(fst)
