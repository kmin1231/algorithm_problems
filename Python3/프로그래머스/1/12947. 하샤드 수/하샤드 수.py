def solution(x):
    strx = str(x)
    y = 0
    for digit in strx:
        y += int(digit)
    answer = True if (x%y == 0) else False
    return answer