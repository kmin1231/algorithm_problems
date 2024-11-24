def solution(numbers):
    answer = []
    num = set()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            num.add(numbers[i] + numbers[j])
    answer = sorted(list(num))
    return answer