from itertools import combinations

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def solution(nums):
    count = 0

    for triple in combinations(nums, 3):
        triple_sum = sum(triple)
        if is_prime(triple_sum): count += 1

    return count