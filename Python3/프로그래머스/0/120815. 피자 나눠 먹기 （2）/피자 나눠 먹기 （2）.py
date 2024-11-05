def solution(n):
    if n%6 == 0: answer = n//6
    else :
        i = 1
        while (n*i)%6 != 0:
            i += 1
        answer = (n*i)//6
    return answer