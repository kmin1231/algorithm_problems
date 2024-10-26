def solution(my_string):
    answer = []
    count = len(my_string)
    for i in range(count):
        answer.append(my_string[-i:])
    answer.sort()
    return answer