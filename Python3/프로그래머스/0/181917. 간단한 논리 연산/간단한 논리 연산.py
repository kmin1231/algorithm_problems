def solution(x1, x2, x3, x4):
    result1 = x1 or x2
    result2 = x3 or x4
    answer = result1 and result2
    return answer