def solution(my_string, index_list):
    answer = ''
    count = len(index_list)
    for i in range(count):
        answer += my_string[index_list[i]]
    return answer