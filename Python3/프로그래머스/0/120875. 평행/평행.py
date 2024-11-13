def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    opt1 = (((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2)))
    opt2 = (((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3)))
    opt3 = (((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4)))
    answer = 1 if (opt1 or opt2 or opt3) else 0
    return answer