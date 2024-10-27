def solution(a, d, included):
    answer = 0
    count = len(included)
    for i in range(count):
        if included[i]: answer += (a + d*i)
        else : continue
    return answer