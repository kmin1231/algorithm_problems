def solution(d, budget):
    count = 0

    # sort 'd' in ascending order to support more departments
    d.sort()

    for value in d:
        if budget >= value:
            budget -= value
            count += 1
        else:
            break
    
    return count