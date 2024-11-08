from math import factorial

def solution(balls, share):
    n, m = balls, share
    answer = factorial(n) / factorial(n-m) / factorial(m)
    return answer