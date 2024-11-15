def solution(numlist, n):
    answer = []
    order = dict()
    
    for i in range(len(numlist)):
        diff = abs(numlist[i] - n)
        order[i] = diff

    ordered = sorted(order.items(),
                    key=lambda item: (item[1], -numlist[item[0]]))
    
    for i, _ in ordered:
        answer.append(numlist[i])
    return answer