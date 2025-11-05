from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    counts = sorted(counter.values(), reverse=True)

    kinds, total = 0, 0

    # start from the largest groups first to MINIMIZE the number of different sizes
    for c in counts:
        total += c
        kinds += 1
        if total >= k: break

    return kinds