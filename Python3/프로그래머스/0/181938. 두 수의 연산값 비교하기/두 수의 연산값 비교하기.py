def solution(a, b):
    result1 = int(str(a) + str(b))
    result2 = 2 * a * b
    answer = result1 if (result1 > result2) else result2
    return answer