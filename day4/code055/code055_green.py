def solution(rny_string):
    gather = ['a', 'e', 'i', 'o', 'u']
    if 'm' in rny_string:
        # 'rn' 다음 문자가 모음인 경우에만 'm'을 'rn'으로 대체
        rn_index = rny_string.find('m')
        if rn_index + 2 < len(rny_string) and rny_string[rn_index + 1] or rn_index + 2 < len(rny_string) and rny_string[rn_index + 2]in gather:
            rny_string = rny_string.replace('m', 'rn')
    return rny_string
