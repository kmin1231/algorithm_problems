from math import gcd
def solution(a, b):
    while gcd(a, b) != 1: a, b = a//gcd(a, b), b//gcd(a, b)
    if (b==1): return 1
    else:
        while b % 2 == 0: b = (b//2)
        while b % 5 == 0: b = (b//5)
        return 1 if (b == 1) else 2