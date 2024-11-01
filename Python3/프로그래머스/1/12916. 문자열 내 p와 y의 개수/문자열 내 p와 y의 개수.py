def solution(s):
    answer = True   # default
    string = s.lower()
    p = string.count("p")
    y = string.count("y")
    if p!=y: answer = False
    return answer