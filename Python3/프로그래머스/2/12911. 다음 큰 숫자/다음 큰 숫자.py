def solution(n):
    count = bin(n).count('1')
    for i in range(n+1, n+10000):
        if bin(i).count('1') == count: return i