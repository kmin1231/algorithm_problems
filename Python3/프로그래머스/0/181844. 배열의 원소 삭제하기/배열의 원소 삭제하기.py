def solution(arr, delete_list):
    answer = []
    for elem in arr:
        if (elem in delete_list): continue
        else : answer.append(elem)
    return answer