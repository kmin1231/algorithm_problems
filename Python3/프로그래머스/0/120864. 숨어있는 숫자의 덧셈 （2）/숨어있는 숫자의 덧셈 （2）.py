def solution(my_string):
    answer = 0
    current_num = ""
    
    for char in my_string:
        if char in "0123456789":
            current_num += char
        else:
            if current_num:
                answer += int(current_num)
                current_num = ""
    if current_num: answer += int(current_num)
    
    return answer