from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)

    for name, kind in clothes:
        clothes_dict[kind] += 1

    count = 1
    for kind in clothes_dict:
        count *= (clothes_dict[kind] + 1)

    answer = count - 1

    return answer