def solution(n, k):
    def convert(n, k):
        result = ''
        while n > 0:
            result = str(n % k) + result
            n //= k
        return result

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    converted = convert(n, k)
    candidates = converted.split('0')
    
    count = 0
    for c in candidates:
        if c != '' and is_prime(int(c)):
            count += 1

    return count