def solution(n):
    composite = []
    for i in range(2, n+1):
        for j in range(2, n):
            if (i !=j) and (i%j == 0):
                composite.append(i)
                break
    answer = len(composite)
    return answer