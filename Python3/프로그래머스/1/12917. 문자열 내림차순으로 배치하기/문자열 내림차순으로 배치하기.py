def solution(s):
    ordered = sorted(list(s), reverse=True)
    answer = ''.join(ordered)
    return answer