def solution(str_list, ex):
    answer = ''
    for elem in str_list:
        if (ex in elem): continue
        else: answer += elem
    return answer