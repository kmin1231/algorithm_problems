from math import gcd
from functools import reduce

def lcm(a, b):
    # a = GCD(a, b) * m, b = GCD(a, b) * n (m, n: coprime)
    # LCM(a, b) = GCD(a, b) * m * n = a * b / GCD(a, b)
    return a * b // gcd(a, b)

def solution(arr):
    return reduce(lcm, arr)