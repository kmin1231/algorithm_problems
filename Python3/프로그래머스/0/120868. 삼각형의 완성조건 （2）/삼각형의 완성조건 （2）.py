def solution(sides):
    lb = abs(sides[0] - sides[1])
    ub = sides[0] + sides[1]
    possible = []
    
    for i in range(lb, ub+1):
        options = sorted([sides[0], sides[1], i])
        if options[2] < options[0] + options[1]:
            possible.append(i)
    answer = len(possible)
    return answer