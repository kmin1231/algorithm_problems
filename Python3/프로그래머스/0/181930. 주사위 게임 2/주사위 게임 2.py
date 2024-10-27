def solution(a, b, c):
    answer = 0
    sum = a + b + c
    sqred = a*a + b*b + c*c
    cubed = a*a*a + b*b*b + c*c*c
    if (a == b):
        if (a == c): answer = sum * sqred * cubed
        else: answer = sum * sqred
    elif (b == c): answer = sum * sqred
    elif (a == c) and (a != b): answer = sum * sqred
    else: answer = sum
    return answer