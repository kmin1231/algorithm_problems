def solution(my_strings, parts):
    answer = ''
    count = len(my_strings)
    for i in range(count):
        [m, n] = parts[i]
        answer += my_strings[i][m:n+1]
    return answer