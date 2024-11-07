def solution(i, j, k):
    answer = 0
    num_list = []
    for i in range(i, j+1):
        num_list += list(str(i))
    answer = num_list.count(str(k))
    return answer