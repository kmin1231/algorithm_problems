def solution(my_string, is_suffix):
    count = len(is_suffix)
    answer = 1 if (my_string[-count:] == is_suffix) else 0
    return answer