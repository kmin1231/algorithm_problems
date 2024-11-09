def solution(numbers):
    prod = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            prod.append(numbers[i] * numbers[j])
    prod.sort(reverse=True)
    answer = prod[0]
    return answer