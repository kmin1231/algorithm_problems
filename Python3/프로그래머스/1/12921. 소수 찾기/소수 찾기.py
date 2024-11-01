def solution(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p <= n):
        if (prime[p] == True):
            for i in range(p+p, n+1, p):
                prime[i] = False
        p += 1
    prime = prime[2:]
    answer = prime.count(True)
    return answer