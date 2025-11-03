def solution(n):
    # n = a + (a+1) + (a+2) + ... + (a+k-1) = (a + (a+k-1)) * k / 2 = k * a + k * (k-1) / 2
    count = 0
    k = 1

    while n > (k * (k-1) // 2):   # natural number
        if (n - k * (k - 1) // 2) % k == 0:
            count += 1
        k += 1
    return count