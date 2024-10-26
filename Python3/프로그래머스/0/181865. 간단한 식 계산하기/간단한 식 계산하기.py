def solution(binomial):
    splitted = binomial.split()
    a, op, b = splitted[0], splitted[1], splitted[2]
    if (op == "+"): answer = int(a) + int(b)
    elif (op == "-"): answer = int(a) - int(b)
    else : answer = int(a) * int(b)
    return answer