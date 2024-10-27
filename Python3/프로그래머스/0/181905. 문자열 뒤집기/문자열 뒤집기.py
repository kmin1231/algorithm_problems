def solution(my_string, s, e):
    answer = my_string[:s]
    flip = my_string[s:e+1]
    flip = flip[::-1]
    answer += flip
    answer += my_string[e+1:]
    return answer