def solution(my_string):
    to_lower = my_string.lower()
    my_list = list(to_lower)
    my_list.sort()
    answer = ''.join(my_list)
    return answer