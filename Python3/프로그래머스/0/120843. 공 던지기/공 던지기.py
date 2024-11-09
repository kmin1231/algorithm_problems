def solution(numbers, k):
    count = 2*k - 1
    idx = count % len(numbers) - 1
    answer = numbers[idx]
    return answer