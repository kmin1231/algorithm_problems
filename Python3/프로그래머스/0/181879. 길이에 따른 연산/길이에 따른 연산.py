def solution(num_list):
    result1, result2 = 0, 1

    if (len(num_list) >= 11):
        for i in num_list:
            result1 += i
            answer = result1
    else:
        for i in num_list:
            result2 *= i
            answer = result2
    return answer