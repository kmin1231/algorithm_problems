def solution(bin1, bin2):
    answer = ''
    num1, num2 = 0, 0
    for i in range(1, len(bin1)+1):
        num1 += int(bin1[-i]) * 2**(i-1)
    for i in range(1, len(bin2)+1):
        num2 += int(bin2[-i]) * 2**(i-1)
    total = num1 + num2
    if total == 0: return '0'
    while total != 0:
        answer += str(total%2)
        total //= 2
    answer = ''.join(reversed(answer))
    return answer