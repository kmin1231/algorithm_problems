def solution(intStrs, k, s, l):
    answer = []
    for elem in intStrs:
        temp = int(elem[s:s+l])
        if (temp > k): answer.append(temp)
        else: continue
    return answer