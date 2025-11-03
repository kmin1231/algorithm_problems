def solution(A, B):
    # greedy algorithm (to minimize total sum)
    A.sort()                # ascending
    B.sort(reverse=True)    # descending

    answer = sum(a * b for a, b in zip(A, B))

    return answer