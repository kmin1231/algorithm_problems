def solution(ineq, eq, n, m):
    if (ineq, eq) == (">", "="): answer = int(n >= m)
    elif (ineq, eq) == ("<", "="): answer = int(n <= m)
    elif (ineq, eq) == (">", "!"): answer = int(n > m)
    else: answer = int(n < m)
    return answer