def solution(n):
    if (n%2 == 0): count = n/2
    else : count = (n-1)/2
    answer = count * (count+1)
    return answer