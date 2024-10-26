def solution(my_string, overwrite_string, s):
    answer = ''
    m = len(overwrite_string)   # length of 'overwrite_string'
    
    answer += my_string[:s]
    answer += overwrite_string
    answer += my_string[s + m:]
    
    return answer