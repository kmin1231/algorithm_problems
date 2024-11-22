def solution(citations):
    answer = 0
    n = len(citations)
    h = 0
    for i in range(1, n+1):
        count =0
        for cite in citations:
            if cite >= i: count += 1
            if count >= i:
                h = i
                break
        if h > answer: answer = h
    return answer