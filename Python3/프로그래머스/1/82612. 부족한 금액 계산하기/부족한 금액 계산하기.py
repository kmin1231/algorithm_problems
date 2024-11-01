def solution(price, money, count):
    charge = price * count * (count+1) / 2
    if money >= charge: answer = 0
    else : answer = charge - money
    return answer