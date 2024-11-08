def solution(my_string):
    answer = []
    for char in my_string:
        if char in "0123456789": answer.append(int(char))
    answer.sort()
    return answer