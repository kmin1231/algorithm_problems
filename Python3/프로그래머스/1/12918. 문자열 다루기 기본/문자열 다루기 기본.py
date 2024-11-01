def solution(s):
    if len(s) != 4 and len(s) != 6: answer = False
    elif not s.isdigit(): answer = False
    else: answer = True
    return answer