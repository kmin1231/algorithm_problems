def solution(myString):
    answer = []
    splitted = myString.split("x")
    for elem in splitted:
        answer.append(len(elem))
    return answer