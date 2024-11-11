def solution(sides):
    ordered = list(sorted(sides))
    answer = 1 if (ordered[2] < (ordered[0] + ordered[1])) else 2
    return answer