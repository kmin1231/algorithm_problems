def solution(num_list, n):
    answer = []
    count = len(num_list)
    for i in range(count):
        if (i%n == 0): answer.append(num_list[i])
    return answer