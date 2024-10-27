def solution(strArr):
    answer = []
    for elem in strArr:
        if ('ad' in elem): continue
        else : answer.append(elem)
    return answer