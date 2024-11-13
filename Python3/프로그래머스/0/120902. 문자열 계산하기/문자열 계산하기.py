def solution(my_string):
    my_list = my_string.split(" ")
    answer = int(my_list[0])   # first number
    operator = None
    
    for elem in my_list[1:]:
        if elem in ["+", "-"]:
            opr = elem
        else:
            if opr == "+": answer += int(elem)
            else : answer -= int(elem)
    return answer