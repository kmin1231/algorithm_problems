def solution(n):
    temp = list(str(n))
    temp.reverse()
    answer = []
    for numStr in temp: answer.append(int(numStr))
    return answer