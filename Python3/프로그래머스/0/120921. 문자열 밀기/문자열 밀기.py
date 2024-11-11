def solution(A, B):
    options = []
    for i in range(len(A)):
        slided = A[-i:] + A[:-i]
        options.append(slided)
    answer = options.index(B) if (B in options) else -1      
    return answer