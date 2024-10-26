def solution(todo_list, finished):
    count = len(todo_list)
    answer = []

    for i in range(count):
        if (finished[i] == False):    # Note: 'boolean' array
            answer.append(todo_list[i])
        else: continue
    return answer