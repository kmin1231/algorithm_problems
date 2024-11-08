def solution(emergency):
    answer = []
    ordered = list(sorted(emergency, reverse=True))
    for i in range(len(emergency)):
        idx = ordered.index(emergency[i])
        print(emergency[i], idx)
        answer.append(idx+1)
    return answer