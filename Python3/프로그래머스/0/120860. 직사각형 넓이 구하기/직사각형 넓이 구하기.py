def solution(dots):
    horizontal, vertical = [], []
    for [x, y] in dots:
        horizontal.append(x)
        vertical.append(y)
    horizontal.sort()
    vertical.sort()
    h = horizontal[-1] - horizontal[0]
    v = vertical[-1] - vertical[0]
    answer = h * v
    return answer