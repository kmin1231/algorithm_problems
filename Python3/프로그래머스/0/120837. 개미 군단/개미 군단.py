def solution(hp):
    type5 = hp // 5
    type3 = (hp - type5 * 5) // 3
    type1 = hp - type5 * 5 - type3 * 3
    answer = type5 + type3 + type1
    return answer