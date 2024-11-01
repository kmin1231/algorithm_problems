def solution(money):
    count = int(money/5500)
    remaining = money - 5500 * count
    answer = [count, remaining]
    return answer