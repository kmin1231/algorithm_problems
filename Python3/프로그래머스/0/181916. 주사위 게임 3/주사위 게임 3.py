def solution(a, b, c, d):
    spot = [a, b, c, d]
    dice = [spot.count(1), spot.count(2), spot.count(3),
             spot.count(4), spot.count(5), spot.count(6)]

    if 4 in dice:
        p = dice.index(4) + 1
        answer = 1111 * p

    elif 3 in dice:
        p = dice.index(3) + 1
        q = dice.index(1) + 1
        answer = (10 * p + q) * (10 * p + q)
    
    elif dice.count(2) == 2:
        p = dice.index(2) + 1
        q = dice.index(2, p) + 1
        answer = (p + q) * abs(p - q)
    
    elif 2 in dice:
        p = dice.index(2) + 1
        q, r = [i + 1 for i in range(6) if dice[i] == 1]
        answer = q * r
    
    elif (dice.count(1) == 4):
        spot.sort()
        answer = spot[0]
    return answer