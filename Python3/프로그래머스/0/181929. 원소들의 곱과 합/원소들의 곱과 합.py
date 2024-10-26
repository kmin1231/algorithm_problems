def solution(num_list):
    result1, result2 = 1, 0
    for num in num_list:
        result1 *= num
        result2 += num
    result2 = result2 * result2
    answer = 1 if (result1 < result2) else 0
    return answer