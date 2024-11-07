def solution(my_string):
    answer = ''
    existing = []
    for char in my_string:
        if char not in existing:
            answer += char
            existing.append(char)
        else : continue
    return answer