def num_divisors(n):
    count = 0

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i == (n // i): count += 1    # perfect square
            else: count += 2

    return count

def solution(number, limit, power):
    total = 0

    for i in range(1, number + 1):
        divisors = num_divisors(i)

        # [NOTE] should be replaced with 'power'
        if divisors > limit: divisors = power

        total += divisors

    return total