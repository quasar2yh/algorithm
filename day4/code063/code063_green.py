def solution(a, b):
    fst = str(a) + str(b)
    snd = str(b) + str(a)
    return max(int(fst),int(snd))
