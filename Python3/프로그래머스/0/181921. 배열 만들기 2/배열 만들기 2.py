from itertools import product

def solution(l, r):
    answer = []
    for i in product([0, 5], repeat=len(str(r))):
        num = int("".join(map(str, i)))
        if (num >= l):
            if (num <= r):
                answer.append(num)
            else:
                break
    if len(answer) == 0: answer = [-1]
    return answer