def solution(numbers):
    products = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            products.append(numbers[i] * numbers[j])
    products.sort(reverse=True)
    answer = products[0]
    return answer