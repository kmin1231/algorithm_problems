def solution(names):
    answer = []
    count = len(names)
    for i in range(count):
        if (i%5 == 0): answer.append(names[i])
    return answer