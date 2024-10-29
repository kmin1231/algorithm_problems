def solution(my_string, queries):
    answer = list(my_string)
    for elem in queries:
        [s, e] = elem
        answer[s:e+1] = list(reversed(answer[s:e+1]))
    answer = ''.join(answer)
    return answer