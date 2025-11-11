def solution(elements):
    n = len(elements)
    extended = elements * 2
    sums = set()

    for length in range(1, n + 1):
        for start in range(n):
            sub_sum = sum(extended[start:start + length])
            sums.add(sub_sum)

    answer = len(sums)
    return answer