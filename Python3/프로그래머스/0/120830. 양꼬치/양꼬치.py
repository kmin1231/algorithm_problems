def solution(n, k):
    yang = 12000 * n
    drink = 2000 * (k - int(n/10))
    return yang + drink