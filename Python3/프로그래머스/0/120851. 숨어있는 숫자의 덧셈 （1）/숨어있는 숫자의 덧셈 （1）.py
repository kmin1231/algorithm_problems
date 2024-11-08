def solution(my_string):
    answer = 0
    for char in my_string:
        if char in "0123456789": answer += int(char)
        else : continue
    return answer