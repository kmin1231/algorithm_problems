def solution(n):
    pairs = []
    for i in range(1, n+1):
        if (n%i == 0): pairs.append((i, 20/i))        
    return len(pairs)