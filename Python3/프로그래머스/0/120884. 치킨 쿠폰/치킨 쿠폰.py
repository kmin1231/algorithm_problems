def solution(chicken):
    coupon = chicken
    answer = 0
    while (coupon >= 10):
        bonus_chicken = coupon//10
        chicken += bonus_chicken
        answer += bonus_chicken
        coupon = coupon - bonus_chicken*10 + bonus_chicken
    return answer