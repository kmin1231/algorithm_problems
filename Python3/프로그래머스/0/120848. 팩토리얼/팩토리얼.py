from math import factorial

def solution(n):
    i=0
    while factorial(i) <= n:
        i += 1
    return i-1