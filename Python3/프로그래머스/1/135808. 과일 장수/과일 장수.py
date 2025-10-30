def solution(k, m, score):
    score.sort(reverse=True)
    total = 0

    # revenue per box
    for i in range(0, len(score), m):
        box = score[i:i+m]

        if len(box) < m: break  # cannot sell

        total += min(box) * m

    return total