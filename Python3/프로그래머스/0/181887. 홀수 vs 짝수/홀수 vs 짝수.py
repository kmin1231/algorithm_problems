def solution(num_list):
    sum1, sum2 = 0, 0
    for i in range(len(num_list)):
        if (i%2 == 0): sum1 += num_list[i]
        else: sum2 += num_list[i]
    if (sum1 > sum2): answer = sum1
    else: answer = sum2
    return answer