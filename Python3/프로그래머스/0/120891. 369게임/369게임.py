def solution(order):
    answer = 0
    num = str(order)
    for digit in num:
     if digit in "369": answer += 1
    return answer