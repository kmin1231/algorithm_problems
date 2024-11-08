def solution(num_list, n):
    answer = []
    for i in range(len(num_list)):
        temp_list = []
        if i%n == 0:
            temp_list = num_list[i:i+n]
            answer.append(temp_list)
    return answer