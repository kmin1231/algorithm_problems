def solution(num_list):
    answer = -1   # default
    for i in range(len(num_list)):
        if (num_list[i] >= 0): continue
        else:
            answer = i
            break
    return answer