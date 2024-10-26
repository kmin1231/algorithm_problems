def solution(my_string, is_prefix):
    length = len(is_prefix)
    if (my_string[:length] == is_prefix): answer = 1
    else: answer = 0 
    return answer