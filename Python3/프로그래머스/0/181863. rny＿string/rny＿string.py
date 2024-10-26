def solution(rny_string):
    answer = rny_string
    for char in rny_string:
        if ('m' in char): answer = rny_string.replace('m', 'rn')
        if ('rn' in char): answer = rny_string.replace('rn', 'm')
    return answer