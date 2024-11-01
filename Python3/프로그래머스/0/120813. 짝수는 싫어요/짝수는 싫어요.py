def solution(n):
    answer = []
    if (n%2 == 0): last = n-1
    else : last = n
    
    i = 1
    while i <= last:
        answer.append(i)
        i += 2
    return answer